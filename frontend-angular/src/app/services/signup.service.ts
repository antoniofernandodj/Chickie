import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export type EmpresaSignUpRequest = {

  nome: string,
  username: string,
  email: string,
  telefone: string,
  celular: string,
  password: string
  
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
  uf: string

}


@Injectable({ providedIn: 'root' })
export class SignupService {

  private companySignupUrl: string
  private userSignupUrl: string

  constructor(private http: HttpClient) {
    this.companySignupUrl = 'http://localhost:8000/loja/signin'
    this.userSignupUrl = 'http://localhost:8000/user/signin'
  }

  doCompanySignUp(body: any) {
    let obs = this.http.post(this.companySignupUrl, body)
    return obs
  }

  doUserSignUp(body: UserSignUpRequest) {
    let obs = this.http.post(this.userSignupUrl, body)
    return obs
  }
}
