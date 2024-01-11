import { AuthService, CompanyAuthData } from './auth.service';

import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';


export type Endereco = {
  uf: string,
  cidade: string,
  logradouro: string,
  numero: string,
  bairro: string,
  cep: string,
  complemento: string,
}

export type PedidoBodyRequest = {
  celular: string,
  data_hora: string,
  endereco: Endereco,
  frete: number,
  itens: Array<{
    produto_uuid: string,
    quantidade: number
  }>,
  loja_uuid: string,
  status_uuid: string | null
}

type PedidoBodyResponse = {
  celular: string,
  data_hora: string,
  endereco: Endereco,
  frete: string,
  itens_pedido: Array<{
    produto_uuid: string,
    quantidade: number
  }>,
  loja_uuid: string
  status_uuid: string | null
  uuid: string,
}

@Injectable({ providedIn: 'root' })
export class PedidoService {

  baseUrl: string
  companyData: CompanyAuthData | null
  token: string

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseUrl = `${environment.host}/pedidos`;
    this.companyData = authService.currentCompany()
    this.token = ''
  }

  getOne(uuid: string) {
    this.companyData = this.authService.currentCompany()
    if (!this.companyData) {
      let msg = 'Dados de empresa não encontrados'
      alert(msg); throw new Error(msg)
    }
    let headers = { Authorization: `Bearer ${this.companyData.access_token}` }

    let observable = this.http.get(
      `${this.baseUrl}/${uuid}`,
      { headers: headers }
    )
    return observable
  }

  getAll(companyUUID: string):Observable<Object> {
    this.companyData = this.authService.currentCompany()
    if (!this.companyData) {
      let msg = 'Dados de empresa não encontrados'
      alert(msg); throw new Error(msg)
    }

    let token = this.companyData.access_token
    let headers = { Authorization: `Bearer ${token}` }
    let params = new HttpParams().set('loja_uuid', companyUUID)
    let observable = this.http.get(`${this.baseUrl}/`, {
      params: params, headers: headers
    })
    return observable
  }

  save(body: PedidoBodyRequest) {
    let observable = this.http.post(`${this.baseUrl}/`, body)
    return observable
  }

  concluir(uuid: string) {
    let headers = { Authorization: `Bearer ${this.companyData?.access_token}` }
    console.log(headers)
    let urlRequest = `${this.baseUrl}/concluir_pedido/${uuid}`
    let observable = this.http.patch(urlRequest, {}, { headers: headers })
    return observable
  }

  delete(item: PedidoBodyResponse) {

    let headers = { Authorization: `Bearer ${this.token}` }

    let observable = this.http.delete(
      `${this.baseUrl}/${item.uuid}`, { headers: headers }
    )
    return observable
  }
}
