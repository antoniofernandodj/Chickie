import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';


export class AuthData {
  access_token: string;
  token_type: string;
  uuid: string;
  nome: string;
  username: string;
  email: string;

  constructor(result: any) {
    this.access_token = result.response.access_token;
    this.token_type = result.response.token_type;
    this.uuid = result.response.uuid;
    this.nome = result.response.nome;
    this.username = result.response.username;
    this.email = result.response.email;
  }

  toString() {
    return JSON.stringify(this)
  }
}


@Injectable({providedIn: 'root'})
export class AuthService {

  isLoggedIn: BehaviorSubject<boolean>
  isLoginPage: BehaviorSubject<boolean>
  userData: BehaviorSubject<AuthData | null>
  companyData: BehaviorSubject<AuthData | null>

  constructor(private http: HttpClient, private router: Router) {
    this.isLoggedIn = new BehaviorSubject(false)
    console.log({"router.url": window.location.pathname})
    this.isLoginPage = new BehaviorSubject(
      window.location.pathname.includes('login')
    )
    this.userData = new BehaviorSubject<AuthData | null>(this.currentUser())
    this.companyData = new BehaviorSubject<AuthData | null>(this.currentCompany())
    this.refreshLoggedIn()
  }

  refreshLoggedIn() {
    this.isLoggedIn.next(!!this.currentCompany() || !!this.currentUser())
    this.userData.next(this.currentUser())
    this.companyData.next(this.currentCompany())
  }

  doCompanyLogin(loginValue: string, passwordValue: string): void {

    const urlLogin = 'http://localhost:8000/loja/login';

    const body = new HttpParams()
      .set('username', loginValue)
      .set('password', passwordValue);

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    };

    let response = this.http.post(urlLogin, body.toString(), httpOptions);

    response.subscribe({
      next: (response) => {
        let token = new AuthData({response});
        sessionStorage.setItem('access_token', token.access_token);
        sessionStorage.setItem('company_data', token.toString());
        this.refreshLoggedIn()
      },
      error: (response) => console.log(response)
    })
  }

  doUserLogin(loginValue: string, passwordValue: string): void {

    const urlLogin = 'http://localhost:8000/user/login';

    const body = new HttpParams()
      .set('username', loginValue)
      .set('password', passwordValue);

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    };

    let response = this.http.post(urlLogin, body.toString(), httpOptions);

    response.subscribe({
      next: (response) => {
        let token = new AuthData({response});
        sessionStorage.setItem('access_token', token.access_token);
        sessionStorage.setItem('user_data', token.toString());
        this.refreshLoggedIn()
      },
      error: (response) => console.log(response)
    })
  }

  doLogout() {
    sessionStorage.clear()
    this.refreshLoggedIn()
  }

  currentCompany() {
    let companyData = sessionStorage.getItem('company_data');
    if (!companyData) {
      return null;
    }
    let data: AuthData = JSON.parse(companyData);
    return data
  }

  currentUser() {
    let userData = sessionStorage.getItem('user_data');
    if (!userData) {
      return null;
    }
    let data: any = JSON.parse(userData);
    return data
  }

}
