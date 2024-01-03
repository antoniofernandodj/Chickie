import { Injectable } from '@angular/core';
import { AuthService, CompanyAuthData } from './auth.service';
import { HttpParams, HttpClient, HttpHeaders } from '@angular/common/http';
import { StatusBodyRequest, StatusResponse } from '../models/status';
import { Observable } from 'rxjs';
import { AuthHeaders } from '../models/authHeaders';


@Injectable({ providedIn: 'root' })
export class StatusService {

  baseUrl: string
  companyData: CompanyAuthData | null
  headers: AuthHeaders

  constructor(private http: HttpClient, private authService: AuthService) {
    this.headers = { Authorization: '' }
    this.baseUrl = 'http://localhost:8000/status'

    this.companyData = this.authService.currentCompany()

    if (this.companyData) {
      this.headers = { Authorization: `Bearer ${this.companyData.access_token}` }
    }

  }

  getOne(uuid: string) {
    let obs = this.http.get(`${this.baseUrl}/${uuid}`)
    return obs
  }

  getAll(companyUUID: string) {
    let params = new HttpParams().set('loja_uuid', companyUUID)
    let obs = this.http.get(`${this.baseUrl}/`, {params: params})
    return obs

  }

  save(body: StatusBodyRequest): Observable<Object> {
    if (!this.companyData) {
      let msg = 'Nenhuma empresa logada!'
      alert(msg); throw new Error(msg)
    }

    return this.http.post(this.baseUrl, body, { headers: this.headers })
  }

  delete(item: StatusResponse) {
    let urlRequest = this.baseUrl.concat(`/${item.uuid}`)
    return this.http.delete(urlRequest, { headers: this.headers })
  }
}
