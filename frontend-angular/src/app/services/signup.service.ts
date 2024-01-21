import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';


export type EmpresaSignUpRequest = {

  nome: string,
  username: string,
  email: string,
  telefone: string,
  celular: string,
  password: string
  image_bytes: string | ArrayBuffer
  image_filename: string

}

export type UserSignUpRequest = {

  celular: string,
  email: string,
  nome: string,
  password: string,
  telefone: string,
  username: string

  bairro: string,
  cep: string,
  cidade: string,
  complemento: string,
  logradouro: string,
  numero: string,
  uf: string,

  modo_de_cadastro: string

}


@Injectable({ providedIn: 'root' })
export class SignupService {

  companySignupUrl: string  = `${environment.host}/loja/signup`
  userSignupUrl: string  = `${environment.host}/user/signup`

  constructor(private http: HttpClient) {
  }

  doCompanySignUp(body: EmpresaSignUpRequest) {
    console.log({'this.companySignupUrl': this.companySignupUrl})
    let obs = this.http.post(this.companySignupUrl, body)
    return obs
  }

  doUserSignUp(body: UserSignUpRequest) {
    console.log({'this.userSignupUrl': this.userSignupUrl})
    let obs = this.http.post(this.userSignupUrl, body)
    return obs
  }

}
