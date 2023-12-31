import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService, AuthData } from './auth.service';


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
  itens_pedido: Array<{
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
  company: AuthData | null
  token: string

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseUrl = 'http://localhost:8000/pedidos'
    this.company = authService.currentCompany()
    this.token = ''
  }

  getOne(uuid: string) {
    this.company = this.authService.currentCompany()
    if (!this.company) {
      let msg = 'Dados de empresa não encontrados'
      alert(msg); throw new Error(msg)
    }
    let headers = { Authorization: `Bearer ${this.company.access_token}` }
    console.log({headers: headers})

    let observable = this.http.get(
      `${this.baseUrl}/${uuid}`,
      { headers: headers }
    )
    return observable
  }

  getAll(companyUUID: string):Observable<Object> {
    this.company = this.authService.currentCompany()
    if (!this.company) {
      let msg = 'Dados de empresa não encontrados'
      alert(msg); throw new Error(msg)
    }

    let token = this.company.access_token
    let headers = { Authorization: `Bearer ${token}` }
    let params = new HttpParams().set('loja_uuid', companyUUID)

    let observable = this.http.get(
      `${this.baseUrl}/`,
      { params: params, headers: headers }
    )
    return observable
  }

  save(body: PedidoBodyRequest) {
    let observable = this.http.post(`${this.baseUrl}/`, body)
    return observable
  }

  delete(item: PedidoBodyResponse) {

    let headers = new HttpHeaders({ Authorization: `Bearer ${this.token}` })

    let observable = this.http.delete(
      `${this.baseUrl}/${item.uuid}`, { headers: headers }
    )
    return observable
  }
}
