import { AuthService, CompanyAuthData } from './auth.service';

import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { PrecoBodyRequest, PrecoResponse } from '../models/models';
import { environment } from '../../environments/environment';


@Injectable({ providedIn: 'root' })
export class PrecoService {

  baseUrl: string
  companyData: CompanyAuthData | null
  token: string
  headers: HttpHeaders

  constructor(
    private http: HttpClient,
    private authService: AuthService,
  ) {
    this.baseUrl = `${environment.host}/precos`
    this.headers = new HttpHeaders({})
    this.companyData = authService.currentCompany()
    this.token = ''
    if (this.companyData) {
      this.token = this.companyData.access_token
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
