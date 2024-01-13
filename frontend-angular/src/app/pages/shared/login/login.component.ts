import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import {  CompanyAuthData, AuthData,
          AuthService } from '../../../services/auth.service';
import { HttpErrorResponse } from '@angular/common/http';
import { ButtonHandler } from '../../../handlers/button';


class ErrorDetail {
  input: null;
  loc: string[];
  msg: string;
  type: string;
  url: string;

  constructor(response: any) {
    this.input = response.input;
    this.loc = response.loc;
    this.msg = response.msg;
    this.type = response.type;
    this.url = response.url;
  }

  showError() {
    let string = `${this.type.toUpperCase()}. ${this.msg}: ${this.loc[1]}`

    alert(string)
  }
}


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, RouterModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.sass'
})
export class LoginComponent {

  loginCompanyValue: string;
  passwordCompanyValue: string;

  loginUserValue: string;
  passwordUserValue: string;

  constructor(private authService: AuthService, private router: Router) {
    this.loginCompanyValue = "";
    this.passwordCompanyValue = "";

    this.loginUserValue= "";
    this.passwordUserValue = "";
  }

  ngOnInit(): void { }

  doCompanyLogin(event: Event): void {

    let button = new ButtonHandler(undefined, 'btn_loja')
    button.disable('Autenticando...')

    this.authService.doCompanyLogin(
      this.loginCompanyValue,
      this.passwordCompanyValue
    ).subscribe({

      next: (response: Object) => {
        button.enable()
        let authData = new CompanyAuthData({ response });
        this.authService.setCompanyData(authData)
        this.authService.refreshLoggedIn();

        this.authService.isLoginPage.next(false);

        this.router.navigate(['/loja/home']);
      },

      error: (response: HttpErrorResponse) => {
        button.enable()
        alert(`${response.statusText}: ${response.error.detail}`)
      },
    });

  }

  doUserLogin(event: Event): void {
    let button = new ButtonHandler(undefined, 'btn_user')
    button.disable('Autenticando...')

    this.authService.doUserLogin(this.loginUserValue, this.passwordUserValue).subscribe({
      next: (response: Object) => {
        button.enable()
        let authData = new AuthData({ response });
        sessionStorage.setItem('access_token', authData.access_token);
        sessionStorage.setItem('current_user', authData.toString());
        this.authService.refreshLoggedIn();

        this.authService.isLoginPage.next(false)
        this.router.navigate(['/user/home']);
      },
      error: (response: HttpErrorResponse) => {
        button.enable()
        let message = response.message

        // if (message) {
        //   alert(`${response.statusText}: ${message}`)
        //   return
        // }

        console.log('veio aqui')
        let detail = response.error.detail
        console.log({detail: detail})
        if (typeof detail == 'string') {
          alert(`${response.statusText}: ${response.error.detail}`)
        }

        if (Array.isArray(detail)) {
          let errArr = detail.map(item => new ErrorDetail(item))
          for (let errorItem of errArr) {
            errorItem.showError()
          }
        }

      },
    });
  }
}
