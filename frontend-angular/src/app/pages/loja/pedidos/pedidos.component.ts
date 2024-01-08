import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { Pedido, StatusResponse } from '../../../models/models';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import {  CompanyAuthData, AuthService, PedidoService,
          ProdutoService, StatusService } from '../../../services/services';


@Component({
  selector: 'app-pedido',
  standalone: true,
  imports: [FormsModule, CommonModule, RouterModule],
  templateUrl: './pedidos.component.html',
  styleUrl: './pedidos.component.sass'
})
export class PedidosComponent {

  pedidoUUID: string | null
  pedidos: BehaviorSubject<Array<Pedido>>
  companyData: CompanyAuthData | null
  statusList: Array<StatusResponse>

  constructor(
    private pedidoService: PedidoService,
    private produtoService: ProdutoService,
    private authService: AuthService,
    private route: ActivatedRoute,
    private statusService: StatusService
  ) {
    this.pedidos = new BehaviorSubject<Array<Pedido>>([])
    this.statusList = []
    this.pedidoUUID = null
    this.companyData = this.authService.currentCompany()
  }

  ngOnInit() {
    this.route.params.subscribe(params => {

      if (!this.companyData) {
        let msg = "Dados de empresa não encontrados"
        alert(msg); throw new Error(msg)
      }

      this.statusService.getAll(this.companyData.loja.uuid).subscribe({
        next: (response) => {
          if (Array.isArray(response)) {
            this.statusList.push(...response)
          }
        },
        error: (response) => {
          throw new Error('Erro na requisição dos dados')
        }
      })

      this.pedidoService.getAll(this.companyData.loja.uuid).subscribe({
        next: (response: any) => {
          this.pedidos.next(response)
          console.log({response: response})
        },
        error: (response) => {
          let msg = 'Erro na busca do pedido'
          alert(msg); console.log(response); throw new Error(msg)
        }
      })
    })
  }

  formatarData(dataISO: string) {
    const data = new Date(dataISO);

    const dia = String(data.getDate()).padStart(2, '0');
    const mes = String(data.getMonth() + 1).padStart(2, '0');
    const ano = data.getFullYear();

    const horas = String(data.getHours()).padStart(2, '0');
    const minutos = String(data.getMinutes()).padStart(2, '0');
    const segundos = String(data.getSeconds()).padStart(2, '0');

    return `${dia}/${mes}/${ano} ${horas}:${minutos}:${segundos}`;
  }

  atualizarStatusDePedido(pedido: any) {
    console.log(pedido)
    alert('Status Atualizado com sucesso!')
  }

  atualizarFreteDePedido(pedido: any) {
    console.log(pedido)
    alert('Frete atualizado com sucesso!')
  }

}
