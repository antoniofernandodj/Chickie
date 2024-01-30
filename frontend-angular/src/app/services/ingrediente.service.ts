import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { UserSignUpRequest } from './signup.service';
import { AuthService, CompanyAuthData } from './auth.service';
import { AuthHeaders } from '../models/authHeaders';
import { IngredienteBodyRequest, Ingrediente } from '../models/models';

@Injectable({ providedIn: 'root' })
export class IngredienteService {

  baseUrl: string
  headers: AuthHeaders
  token: string
  companyData: CompanyAuthData | null

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) {
    this.baseUrl = `${environment.host}/ingredientes`
    this.headers = { Authorization: ''}
    this.companyData = authService.currentCompany()

    this.token = ''
    if (this.companyData) {
      this.token = this.companyData.access_token
      this.headers = { Authorization: `Bearer ${this.token}` }
    }

  }

  getOne(uuid: string) {
    let observable = this.http.get(`${this.baseUrl}/${uuid}`)
    observable.subscribe({
      next: (res) => {console.log(res)},
      error: (res) => {console.error(res)}
    })
  }

  getAll(produtoUUID: string):Observable<Object> {
    let params = {'produto_uuid': produtoUUID}
    let observable = this.http.get(this.baseUrl, {params: params})
    return observable
  }

  save(body: IngredienteBodyRequest) {
    let observable = this.http.post(
      this.baseUrl, body, { headers: this.headers }
    )
    return observable
  }

  delete(ingrediente: Ingrediente) {
    let urlRequest = `${this.baseUrl}/${ingrediente.uuid}`
    let observable = this.http.delete(urlRequest, { headers: this.headers })
    return observable
  }

}
