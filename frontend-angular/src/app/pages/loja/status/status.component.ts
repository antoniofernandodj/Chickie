import { Component } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { Response201Wrapper, StatusResponse } from '../../../models/models';

import {  AuthService, CompanyAuthData,
          StatusService } from '../../../services/services';


@Component({
  selector: 'app-status',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './status.component.html',
  styleUrl: './status.component.sass'
})
export class StatusComponent {

  companyData: CompanyAuthData | null
  statusList: BehaviorSubject<Array<StatusResponse>>
  descricaoValue: string
  nomeValue: string
  saving: boolean
  fetching: boolean

  constructor(private statusService: StatusService, private authService: AuthService) {
    this.saving = false
    this.fetching = false
    this.descricaoValue = ''
    this.nomeValue = ''
    this.companyData = authService.currentCompany();
    this.statusList = new BehaviorSubject<Array<StatusResponse>>([])
  }

  ngOnInit(): void {
    this.fetching = true
    if (this.companyData === null) {
      let msg = 'Dados da empresa não encontrados!'
      alert(msg); throw new Error(msg)
    }
    this.statusService.getAll(this.companyData.loja.uuid).subscribe({
      next: (response) => {
        if (Array.isArray(response)) {
          this.statusList.value.push(...response)
        }
        this.fetching = false
      },
      error: (response) => {
        throw new Error('Erro na requisição dos dados')
      }
    })

  }

  public cadastrarStatus(): void {
    this.saving = true
    if (!this.companyData) {
      this.saving = false
      let msg = 'Dados da empresa não encontrados!'
      alert(msg); throw new Error(msg)
    }

    let body = {
      loja_uuid: this.companyData.loja.uuid,
      descricao: this.descricaoValue,
      nome: this.nomeValue
    }

    this.statusService.save(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        let newStatusItem = {...body, uuid: r.uuid}
        this.statusList.value.push(newStatusItem)
        alert('Item cadastrado com sucesso!')
        this.saving = false
      },
      error: (response) => {
        this.saving = false
        let msg = 'Erro no cadastro do item';
        alert(msg); throw new Error(msg)
      }
    })
  }

  public deletarStatus(event: Event, status: StatusResponse): void {

    let button = event.target as HTMLButtonElement

    let initialHTML = button.innerHTML

    button.disabled = true
    button.innerHTML = 'Removendo...'

    this.statusService.delete(status).subscribe({
      next: (response) => {
        let newList = this.statusList.value
        .filter(item => item.uuid !== status.uuid);

        this.statusList.next(newList);
        alert('Item removido com sucesso!')
      },
      error: (response) => {
        let msg = 'Erro na remoção do item';

        button.disabled = false
        button.innerHTML = initialHTML

        alert(msg); throw new Error(msg)
      }
    })
  }
}
