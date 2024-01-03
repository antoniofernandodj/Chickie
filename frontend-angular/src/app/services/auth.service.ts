import { Injectable } from '@angular/core';
import { AuthHeaders } from '../models/authHeaders';
import { Observable, BehaviorSubject } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { LojaService } from './loja.service';
import {
  HttpClient,
  HttpParams,
  HttpHeaders,
  HttpErrorResponse,
  HttpResponse
} from '@angular/common/http';




type Endereco = {
  bairro: string
  cep: string
  cidade: string
  complemento: string
  logradouro: string
  numero: string
  uf: string
  uuid: string
}


type Loja = {
  celular: string;
  email: string;
  endereco: Endereco;
  imagem_cadastro: string;
  nome: string;
  telefone: string;
  username: string;
  uuid: string;
}


export class CompanyAuthData {
  access_token: string;
  token_type: string;
  loja: Loja;

  constructor(result: any) {
    this.access_token = result.response.access_token;
    this.token_type = result.response.token_type;
    this.loja = result.response.loja;
  }

  toString() {
    return JSON.stringify(this);
  }
}


export class AuthData {
  access_token: string;
  token_type: string;
  celular: string;
  uuid: string;
  nome: string;
  username: string;
  email: string;
  endereco: any

  constructor(result: any) {
    this.access_token = result.response.access_token;
    this.celular = result.response.celular;
    this.token_type = result.response.token_type;
    this.uuid = result.response.uuid;
    this.nome = result.response.nome;
    this.username = result.response.username;
    this.email = result.response.email;
    this.endereco = result.response.endereco
  }

  toString() {
    return JSON.stringify(this);
  }
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  companyIsLoggedIn: BehaviorSubject<boolean>;
  userIsLoggedIn: BehaviorSubject<boolean>;
  isLoginPage: BehaviorSubject<boolean>;
  userData: BehaviorSubject<AuthData | null>;
  companyData: BehaviorSubject<CompanyAuthData | null>;
  loja_uuid: string | null

  constructor(
    private http: HttpClient,
    private route: ActivatedRoute,
    private router: Router,
    private lojaService: LojaService
  ) {
    this.loja_uuid = null
    this.companyIsLoggedIn = new BehaviorSubject(false);
    this.userIsLoggedIn = new BehaviorSubject(false);
    this.isLoginPage = new BehaviorSubject(
      window.location.pathname.includes('login')
    );
    this.userData = new BehaviorSubject<AuthData | null>(this.currentUser());
    this.companyData = new BehaviorSubject<CompanyAuthData | null>(this.currentCompany());
    this.refreshLoggedIn();
  }

  refreshLoggedIn() {
    this.companyIsLoggedIn.next(!!this.currentCompany());
    this.userIsLoggedIn.next(!!this.currentUser());
    this.userData.next(this.currentUser());
    this.companyData.next(this.currentCompany());
  }

  setCompanyData(companyData: CompanyAuthData) {
    let dataString = JSON.stringify(companyData);
    sessionStorage.setItem('access_token', companyData.access_token);
    sessionStorage.setItem('current_company', dataString);
    this.refreshLoggedIn();
  }

  doCompanyLogin(loginValue: string, passwordValue: string): Observable<Object> {
    const urlLogin = 'http://localhost:8000/loja/login';

    const body = new HttpParams()
      .set('username', loginValue)
      .set('password', passwordValue);

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded',
      }),
    };

    return this.http.post(urlLogin, body.toString(), httpOptions);
  }

  doUserLogin(loginValue: string, passwordValue: string): Observable<Object> {
    const urlLogin = 'http://localhost:8000/user/login';

    const body = new HttpParams()
      .set('username', loginValue)
      .set('password', passwordValue);

    const headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    const httpOptions = { headers: headers };

    return this.http.post(urlLogin, body.toString(), httpOptions);
  }

  doLogout() {
    sessionStorage.clear();
    this.refreshLoggedIn();
  }

  currentCompany() {
    let companyData = sessionStorage.getItem('current_company');
    if (!companyData) {
      return null;
    }
    let data: CompanyAuthData = JSON.parse(companyData);
    return data;
  }

  getCompanyData(): Promise<CompanyAuthData> {
    return new Promise((resolve, reject) => {
      this.route.params.subscribe(params => {
        this.loja_uuid = params['lojaID'];
        console.log({params: params})

        if (this.loja_uuid) {
          this.lojaService.getOne(this.loja_uuid).subscribe({
            next: (response: any) => {
              let authData = new CompanyAuthData(response);
              resolve(authData);
            },
            error: (err: any) => {
              reject('Erro ao obter os dados da loja');
            }
          })
        } else {
          reject('UUID da loja não encontrado');
        }
      });
    });
  }

  currentUser() {
    let userData = sessionStorage.getItem('current_user');
    if (!userData) {
      return null;
    }
    let data: any = JSON.parse(userData);
    return data;
  }
}
