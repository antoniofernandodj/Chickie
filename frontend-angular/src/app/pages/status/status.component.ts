import { Component } from '@angular/core';
import { StatusService } from '../../services/status.service';
import { StatusBodyRequest, StatusResponse } from '../../models/status';
import { BehaviorSubject } from 'rxjs';
import { AuthService, AuthData } from '../../services/auth.service';
import { FormsModule } from '@angular/forms';
import { Response201Wrapper } from '../../models/wrapper';


@Component({
  selector: 'app-status',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './status.component.html',
  styleUrl: './status.component.sass'
})
export class StatusComponent {

  companyData: AuthData | null
  statusList: BehaviorSubject<Array<StatusResponse>>
  descricaoValue: string
  nomeValue: string

  constructor(private statusService: StatusService, private authService: AuthService) {
    this.descricaoValue = ''
    this.nomeValue = ''
    this.companyData = authService.currentCompany();
    this.statusList = new BehaviorSubject<Array<StatusResponse>>([])
    if (this.companyData === null) {
      throw new Error('Dados da empresa não encontrados!')
    }
    statusService.getAll(this.companyData.uuid).subscribe({
      next: (response) => {
        if (Array.isArray(response)) {
          this.statusList.value.push(...response)
        }
      },
      error: (response) => {
        throw new Error('Erro na requisição dos dados')
      }
    })
  }

  cadastrarStatus() {
    if (this.companyData === null) {
      throw new Error('Dados da empresa não encontrados!')
    }

    let body = {
      loja_uuid: this.companyData.uuid,
      descricao: this.descricaoValue,
      nome: this.nomeValue
    }

    this.statusService.save(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        let newItem = {...body, uuid: r.uuid}
        this.statusList.value.push(newItem)
        alert('Item cadastrado com sucesso!')
      },
      error: (response) => {}
    })
  }

  deletarStatus(status: StatusResponse) {
    this.statusService.delete(status).subscribe({
      next: (response) => {
        let newList = this.statusList.value
        .filter(item => item.uuid !== status.uuid);

        this.statusList.next(newList);
        alert('Item removido com sucesso!')
      },
      error: (response) => {
        let msg = 'Erro na remoção do item';
        alert(msg); throw new Error(msg)
      }
    })
  }
}
