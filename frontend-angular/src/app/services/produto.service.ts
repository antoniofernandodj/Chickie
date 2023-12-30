import { Injectable } from '@angular/core';
import { AuthService, AuthData } from './auth.service';
import { HttpParams, HttpClient, HttpHeaders } from '@angular/common/http';
import { ProdutoBodyRequest, ProdutoResponse } from '../models/produto';
import { Observable } from 'rxjs';


@Injectable({providedIn: 'root'})
export class ProdutoService {

  baseUrl: string
  companyData: AuthData | null
  headers: HttpHeaders

  constructor(private http: HttpClient, private authService: AuthService) {
    this.headers = new HttpHeaders()
    this.baseUrl = 'http://localhost:8000/produtos'
    this.companyData = null
    this.companyData = this.authService.currentCompany()
    if (this.companyData === null) {
      throw new Error('Erro na inicialização ao serviço')
    }
    this.headers = new HttpHeaders(
      {'Authorization': `Bearer ${this.companyData.access_token}`}
    )
  }

  getOne(uuid: string) {
    let obs = this.http.get(`${this.baseUrl}/${uuid}`)
    return obs
  }

  getAll(companyUUID: string, categoryUUID?: string) {
    console.log({companyUUID: companyUUID, categoryUUID: categoryUUID})
    let params = new HttpParams().set('loja_uuid', companyUUID)

    if (categoryUUID) {
      params = params.append('categoria_uuid', categoryUUID);
    }

    let obs = this.http.get(`${this.baseUrl}/`, {params: params})
    return obs

  }

  save(body: ProdutoBodyRequest): Observable<Object> {
    if (!this.companyData) {
      alert('Nenhuma empresa logada!')
      throw new Error('Nenhuma empresa logada!')
    }

    return this.http.post(this.baseUrl, body, { headers: this.headers })
  }

  update() { }

  delete(item: ProdutoResponse) {
    let urlRequest = this.baseUrl.concat(`/${item.uuid}`)
    return this.http.delete(urlRequest, { headers: this.headers })
  }
}
