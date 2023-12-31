import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SignupService } from '../../services/signup.service';
import { AuthService } from '../../services/auth.service';
import { Response201Wrapper } from '../../models/wrapper';


@Component({
  selector: 'app-signup-user',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './signup-user.component.html',
  styleUrl: './signup-user.component.sass'
})
export class SignupUserComponent {

  usernameValue: string
  emailValue: string
  passwordValue: string
  password2Value: string
  nomeValue: string
  celularValue: string
  telefoneValue: string
  cepValue: string
  logradouroValue: string
  numeroValue: string
  complementoValue: string
  bairroValue: string
  cidadeValue: string
  ufValue: string


  constructor(private service: SignupService, private authService: AuthService) {
    this.usernameValue = ''
    this.emailValue = ''
    this.passwordValue = ''
    this.password2Value = ''
    this.nomeValue = ''
    this.celularValue = ''
    this.telefoneValue = ''
    this.cepValue = ''
    this.logradouroValue = ''
    this.numeroValue = ''
    this.complementoValue = ''
    this.bairroValue = ''
    this.cidadeValue = ''
    this.ufValue = ''
  }

  doSignUp() {
    if (this.passwordValue != this.password2Value) {
      alert('A senha e a confirmação não são iguais')
      return
    }

    let body = {

      celular: this.celularValue,
      email: this.emailValue,
      nome: this.nomeValue,
      password: this.passwordValue,
      telefone: this.telefoneValue,
      username: this.usernameValue,

      bairro: this.bairroValue,
      cep: this.cepValue,
      cidade: this.cidadeValue,
      complemento: this.complementoValue,
      logradouro: this.logradouroValue,
      numero: this.numeroValue,
      uf: this.ufValue

    }

    this.service.doUserSignUp(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        alert("Cadastro realizado com sucesso!")
        this.authService.doUserLogin(this.usernameValue, this.passwordValue)
      },
      error: (response) => {
        let msg = "Erro no processamento dos dados!"
        alert(msg); throw new Error(msg)
      }
    })
  }
}
