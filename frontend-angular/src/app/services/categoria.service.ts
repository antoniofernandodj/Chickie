import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService, AuthData } from './auth.service';
import { CategoriaBodyRequest, CategoriaResponse } from '../models/categoria';


@Injectable({ providedIn: 'root' })
export class CategoriaService {

  baseUrl: string
  company: AuthData | null
  token: string

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseUrl = 'http://localhost:8000/categorias'
    this.company = authService.currentCompany()
    this.token = ''
    if (this.company) {
      this.token = this.company.access_token
    }
  }

  getOne(uuid: string) {
    let obs = this.http.get(`${this.baseUrl}/${uuid}`)
    return obs
  }

  getAll(companyUUID: string):Observable<Object> {
    let params = new HttpParams()
      .set('loja_uuid', companyUUID)

    let observable = this.http.get(`${this.baseUrl}/`, {params: params})
    return observable
  }

  save(body: CategoriaBodyRequest) {
    let observable = this.http.post(
      this.baseUrl, body, { headers: { Authorization: `Bearer ${this.token}` } }
    )
    return observable
  }

  delete(item: CategoriaResponse) {

    let observable = this.http.delete(
      `${this.baseUrl}/${item.uuid}`,
      { headers: { Authorization: `Bearer ${this.token}` } }
    )
    return observable
  }
}

