import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService, AuthData } from './auth.service';

type PedidoBodyRequest = {
  data_hora: string,
  endereco_uuid: string,
  frete: string,
  loja_uuid: string
  status_uuid: string
}

type PedidoBodyResponse = {
  uuid: string,
  data_hora: string,
  endereco_uuid: string,
  frete: string,
  loja_uuid: string
  status_uuid: string
}

@Injectable({ providedIn: 'root' })
export class PedidoService {

  baseUrl: string
  company: AuthData | null
  token: string
  headers: HttpHeaders

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseUrl = 'http://localhost:8000/pedidos'
    this.company = authService.currentCompany()
    this.token = ''
    this.headers = new HttpHeaders()
    if (this.company) {
      this.token = this.company.access_token
      this.headers.set('Authorization', `Bearer ${this.token}`)
    }
  }

  getOne(uuid: string) {
    let observable = this.http.get(
      `${this.baseUrl}/${uuid}`,
      { headers: this.headers }
    )
    return observable
  }

  getAll(companyUUID: string):Observable<Object> {
    let params = new HttpParams()
      .set('loja_uuid', companyUUID)

    let observable = this.http.get(
      `${this.baseUrl}/`,
      { params: params, headers: this.headers }
    )
    return observable
  }

  save(body: PedidoBodyRequest) {
    let observable = this.http.post(`${this.baseUrl}/`, body)
    return observable
  }


  delete(item: PedidoBodyResponse) {
    let observable = this.http.delete(
      `${this.baseUrl}/${item.uuid}`,
      { headers: this.headers }
    )
    return observable
  }
}
