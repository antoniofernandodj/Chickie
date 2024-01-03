import { Component } from '@angular/core';
import { AuthService, AuthData } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';
import { LojaService } from '../../services/loja.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';


type Endereco = {
  uf: string;
  cidade: string;
  logradouro: string;
  numero: string;
  bairro: string;
  cep: string;
  complemento: string;
  uuid: string;
}

type Loja = {
  nome: string;
  username: string;
  email: string;
  celular: string;
  uuid: string;
  endereco: Endereco;
  telefone: string;
  imagem_cadastro: string | null;
}


@Component({
  selector: 'app-user-home',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './userHome.component.html',
  styleUrl: './userHome.component.sass'
})
export class UserHomeComponent {

  userData: BehaviorSubject<AuthData | null>
  lojas: BehaviorSubject<Array<Loja>>

  constructor (private authService: AuthService, private lojaService: LojaService) {
    this.userData = authService.userData
    this.lojas = new BehaviorSubject<Array<Loja>>([])
  }

  ngOnInit() {
    this.lojaService.getAll().subscribe({
      next: (response: any) => {
        this.lojas.next(response);
      },
      error: (response) => {
        alert('Erro na requisição dos dados');
        console.log({response: response})
      }
    })
  }
}
