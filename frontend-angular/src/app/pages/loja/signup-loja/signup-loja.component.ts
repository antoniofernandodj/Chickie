import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';
import { NgxMaskDirective } from 'ngx-mask';

import {  FormGroup, FormBuilder,
          ReactiveFormsModule, FormsModule } from '@angular/forms';

import {  SignupService, AuthService, ImageService,
          CompanyAuthData  } from '../../../services/services';

import { Response201Wrapper } from '../../../models/models';


@Component({
  selector: 'app-signup-empresa',
  standalone: true,
  imports: [FormsModule, ReactiveFormsModule, NgxMaskDirective],
  templateUrl: './signup-loja.component.html',
  styleUrl: './signup-loja.component.sass'
})
export class SignupLojaComponent {

  nomeValue: string
  emailValue: string
  telefoneValue: string
  celularValue: string
  usernameValue: string
  senhaValue: string
  senha2Value: string
  selectedImage: string
  imageBytesBase64: string
  imageForm: FormGroup;
  imageFilename: string

  ufValue: string
  cepValue: string
  cidadeValue: string
  logradouroValue: string
  bairroValue: string
  numeroValue: string
  complementoValue: string
  companyLoginStart: boolean
  ufs: Array<string>

  constructor(
    private service: SignupService,
    private authService: AuthService,
    private formBuilder: FormBuilder,
    private imageService: ImageService,
    private router: Router
  ) {

    this.nomeValue = ''
    this.emailValue = ''
    this.telefoneValue = ''
    this.celularValue = ''
    this.usernameValue = ''
    this.senhaValue = ''
    this.senha2Value = ''
    this.selectedImage = ''
    this.imageBytesBase64 = ''
    this.imageFilename = ''

    this.ufValue = 'AC'
    this.cepValue = ''
    this.cidadeValue = ''
    this.logradouroValue = ''
    this.bairroValue = ''
    this.numeroValue = ''
    this.complementoValue = ''
    this.companyLoginStart = false

    this.ufs = [
      'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF',
      'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
      'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS',
      'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ];

    this.imageForm = this.formBuilder.group({ imageFile: [''] });

  }

  async onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.imageFilename = file.name
      this.selectedImage = URL.createObjectURL(file)
      this.imageBytesBase64 = await this.imageService.getImageBytes(file)
    }
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
      password: this.senhaValue,

      uf: this.ufValue,
      cep: this.cepValue,
      cidade: this.cidadeValue,
      logradouro: this.logradouroValue,
      bairro: this.bairroValue,
      numero: this.numeroValue,
      complemento: this.complementoValue,

      image_filename: this.imageFilename,
      image_bytes: this.imageBytesBase64.replace(
        'data:image/jpeg;base64,', ''
      ),
    }

    this.service.doCompanySignUp(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        alert("Cadastro realizado com sucesso!")
        this.authService.doCompanyLogin(this.usernameValue, this.senhaValue).subscribe({
          next: (response: Object) => {

            let authData = new CompanyAuthData({ response });
            this.authService.setCompanyData(authData)
            this.authService.isLoginPage.next(false);
            this.companyLoginStart = false;

            this.router.navigate(['/loja/home']);
          },

          error: (response: HttpErrorResponse) => {
            this.companyLoginStart = false;
            alert(`${response.statusText}: ${response.error.detail}`)
          },
        });
      },
      error: (response) => {
        console.log(response)
        let msg = "Erro no processamento dos dados!"
        alert(msg); throw new Error(msg)
      }
    })
  }
}
