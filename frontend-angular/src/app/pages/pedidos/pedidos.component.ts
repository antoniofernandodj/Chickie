import { Component } from '@angular/core';
import { PedidoService } from '../../services/pedido.service';
import { ProdutoService } from '../../services/produto.service';
import { ActivatedRoute } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { CompanyAuthData, AuthService } from '../../services/auth.service';
import { ProdutoResponse } from '../../models/produto';
import { StatusService } from '../../services/status.service';
import { StatusResponse } from '../../models/status';
import { FormsModule } from '@angular/forms';


export type Pedido = {
  celular: string;
  data_hora: string;
  total: number;
  totalFormatado: string;
  endereco_uuid: string | null;
  endereco: {
    bairro: string;
    cep: string,
    cidade: string;
    uf: string;
    logradouro: string;
    numero: string;
    complemento: string;
    uuid: string
  };
  frete: number;
  itens_pedido: Array<{
    loja_uuid: string;
    pedido_uuid: string;
    produto_uuid: string;
    produto: ProdutoResponse;
    subtotal: any;
    quantidade: number;
    uuid: string;
  }>;
  loja_uuid: string;
  status_uuid: string | null;
  status: any;
  uuid: string;
};


@Component({
  selector: 'app-pedido',
  standalone: true,
  imports: [FormsModule],
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
          this.fetchProducts()
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

  toCurrencyString(number: number): string {
    return `R$${Number(number).toFixed(2)}`.replace('.', ',')
  }

  fetchProducts() {
    for (let pedido of this.pedidos.value) {

      pedido.data_hora = this.formatarData(pedido.data_hora)
      pedido.total = pedido.frete

      for (let item of pedido.itens_pedido) {
        this.produtoService.getOne(item.produto_uuid).subscribe({
          next: (response: any) => {

            item.produto = {
              uuid: response.uuid,
              loja_uuid: response.loja_uuid,
              categoria_uuid: response.categoria_uuid,
              nome: response.nome,
              preco: response.preco,
              descricao: response.descricao,
              categoria: response.categoria,
              image_url: response.image_url
            }
            item.subtotal = Number(response.preco * item.quantidade)
            pedido.total += item.subtotal
            pedido.totalFormatado = this.toCurrencyString(pedido.total)

          },
          error: (response) => {
            console.log({response: response})
          }
        })
      }
      if (pedido.status_uuid == null) {
        pedido.status_uuid = ''
      }
    }
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
