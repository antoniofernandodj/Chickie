import { Component } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { RouterModule } from '@angular/router';

import {  AuthService, AuthData,
          LojaService } from '../../../services/services';

import { LojaResponse } from '../../../models/models';


@Component({
  selector: 'app-user-home',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.sass'
})
export class UserHomeComponent {

  userData: BehaviorSubject<AuthData | null>
  lojas: BehaviorSubject<Array<LojaResponse>>

  constructor (
    private authService: AuthService,
    private lojaService: LojaService
  ) {
    this.userData = authService.userData
    this.lojas = new BehaviorSubject<Array<LojaResponse>>([])
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
