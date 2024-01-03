import { Injectable } from '@angular/core';
import { AuthService, CompanyAuthData } from './auth.service';
import { HttpParams, HttpClient, HttpHeaders } from '@angular/common/http';
import { ProdutoBodyRequest, ProdutoResponse } from '../models/produto';
import { Observable } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { AuthHeaders } from '../models/authHeaders';



@Injectable({ providedIn: 'root' })
export class ProdutoService {

  baseUrl: string
  companyData: CompanyAuthData | null
  headers: AuthHeaders

  constructor(
    private http: HttpClient,
    private authService: AuthService,
    private route: ActivatedRoute
  ) {
    this.headers = { Authorization: ''}
    this.baseUrl = 'http://localhost:8000/produtos'
    this.companyData = null
    this.companyData = this.authService.currentCompany()
    if (this.companyData) {
      this.headers = {
        'Authorization': `Bearer ${this.companyData.access_token}`}
      }
    }

  getOne(uuid: string) {
    let obs = this.http.get(`${this.baseUrl}/${uuid}`)
    return obs
  }

  getAll(companyUUID: string, categoryUUID?: string) {
    let params = new HttpParams().set('loja_uuid', companyUUID)

    if (categoryUUID) {
      params = params.append('categoria_uuid', categoryUUID);
    }

    let obs = this.http.get(`${this.baseUrl}/`, {params: params})
    return obs

  }

  save(body: ProdutoBodyRequest): Observable<Object> {
    return this.http.post(this.baseUrl, body, { headers: this.headers })
  }

  delete(item: ProdutoResponse) {
    let urlRequest = this.baseUrl.concat(`/${item.uuid}`)
    return this.http.delete(urlRequest, { headers: this.headers })
  }
}
