import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SignupService } from '../../services/signup.service';
import { Response201Wrapper } from '../../models/wrapper';
import { AuthData, AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-signup-empresa',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './signup-empresa.component.html',
  styleUrl: './signup-empresa.component.sass'
})
export class SignupEmpresaComponent {

  nomeValue: string
  emailValue: string
  telefoneValue: string
  celularValue: string
  usernameValue: string
  senhaValue: string
  senha2Value: string

  constructor(private service: SignupService, private authService: AuthService) {
    this.nomeValue = ''
    this.emailValue = ''
    this.telefoneValue = ''
    this.celularValue = ''
    this.usernameValue = ''
    this.senhaValue = ''
    this.senha2Value = ''
  }

  doSignUp() {
    if (this.senha2Value != this.senhaValue) {
      alert('A senha e a confirmação não são iguais')
      return
    }

    let body = {
      nome: this.nomeValue,
      email: this.emailValue,
      telefone: this.telefoneValue,
      celular: this.celularValue,
      username: this.usernameValue,
      password: this.senhaValue
    }

    this.service.doCompanySignUp(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        alert("Cadastro realizado com sucesso!")
        this.authService.doCompanyLogin(this.usernameValue, this.senhaValue)
      },
      error: (response) => {
        console.log(response)
        let msg = "Erro no processamento dos dados!"
        alert(msg); throw new Error(msg)
      }
    })
  }
}
