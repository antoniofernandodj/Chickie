import { AuthService, CompanyAuthData } from './auth.service';

import { Injectable } from '@angular/core';
import { HttpParams, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { environment } from '../../environments/environment';

import {  ProdutoBodyRequest, ProdutoPUTRequest,
          ProdutoResponse, AuthHeaders, FileDataRequest } from '../models/models';



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
    this.baseUrl = `${environment.host}/produtos`
    this.companyData = null
    this.companyData = this.authService.currentCompany()
    if (this.companyData) {
      this.headers = {
        'Authorization': `Bearer ${this.companyData.access_token}`}
      }
      console.log({headers: this.headers})
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

    console.log({ headers: this.headers })

    return this.http.post(this.baseUrl, body, { headers: this.headers })
  }

  removeImage(uuid: string) {
    let urlRequest = this.baseUrl.concat(`/${uuid}/imagem`)
    return this.http.delete(urlRequest, { headers: this.headers })
  }

  update(uuid: string, body: ProdutoPUTRequest) {
    let urlRequest = this.baseUrl.concat(`/${uuid}`)
    return this.http.put(urlRequest, body, { headers: this.headers })
  }

  uploadImage(uuid: string, body: FileDataRequest) {
    let urlRequest = this.baseUrl.concat(`/${uuid}/imagem`)
    return this.http.post(urlRequest, body, { headers: this.headers })
  }

  delete(item: ProdutoResponse) {
    let urlRequest = this.baseUrl.concat(`/${item.uuid}`)
    return this.http.delete(urlRequest, { headers: this.headers })
  }
}
