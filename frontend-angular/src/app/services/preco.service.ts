import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService, AuthData } from './auth.service';
import { PrecoBodyRequest, PrecoResponse } from '../models/preco';


@Injectable({providedIn: 'root'})
export class PrecoService {

  baseUrl: string
  company: AuthData | null
  token: string
  headers: HttpHeaders

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) {
    this.baseUrl = 'http://localhost:8000/precos'
    this.headers = new HttpHeaders({})
    this.company = authService.currentCompany()
    this.token = ''
    if (this.company) {
      this.token = this.company.access_token
      this.headers = new HttpHeaders({ Authorization: `Bearer ${this.token}` })
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
    let params = new HttpParams().set('produto_uuid', produtoUUID)
    let observable = this.http.get(this.baseUrl, {params: params})
    return observable
  }

  save(body: PrecoBodyRequest) {
    let observable = this.http.post(this.baseUrl, body, { headers: this.headers })
    return observable
  }

  delete(item: PrecoResponse) {
    let urlRequest = `${this.baseUrl}/${item.uuid}`
    let observable = this.http.delete(urlRequest, { headers: this.headers })
    return observable
  }
}
