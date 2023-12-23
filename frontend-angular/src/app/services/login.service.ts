import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';



class Token {
  access_token: string;
  token_type: string;
  uuid: string;

  constructor(result: any) {
    this.access_token = result.response.access_token;
    this.token_type = result.response.token_type;
    this.uuid = result.response.uuid;
  }
}



@Injectable({providedIn: 'root'})
export class LoginService {

  constructor(private http: HttpClient, private router: Router) {}

  doLogin(loginValue: string, passwordValue: string): void {

    const urlLogin = 'http://localhost:8000/loja/login';

    const body = new HttpParams()
      .set('username', loginValue)
      .set('password', passwordValue);

    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    };

    let response = this.http.post(urlLogin, body.toString(), httpOptions)

    response.subscribe({
      next: (response) => this.successLogin(response),
      error: (response) => this.failLogin(response)
    })
  }

  successLogin(response: Object) {
    let token = new Token({response})
    sessionStorage.setItem('access_token', token.access_token)
    sessionStorage.setItem('user_uuid', token.uuid)
    this.router.navigate(['/']);
  }

  failLogin(response: Object) {
    let token = new Token({response})
    console.log(token)
  }
}
