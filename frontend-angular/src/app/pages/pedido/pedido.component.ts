import { Component } from '@angular/core';
import { PedidoService } from '../../services/pedido.service';
import { ProdutoService } from '../../services/produto.service';
import { ActivatedRoute } from '@angular/router';
import { BehaviorSubject } from 'rxjs';


export type Pedido = {
  celular: string;
  data_hora: string;
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
    produto: any;
    subtotal: any;
    quantidade: number;
    uuid: string;
  }>;
  loja_uuid: string;
  status_uuid: string | null;
  uuid: string;
};


@Component({
  selector: 'app-pedido',
  standalone: true,
  imports: [],
  templateUrl: './pedido.component.html',
  styleUrl: './pedido.component.sass'
})
export class PedidoComponent {

  pedidoUUID: string | null
  pedido: Pedido | null
  total: BehaviorSubject<number>
  totalFormatado: BehaviorSubject<string>

  constructor(
    private pedidoService: PedidoService,
    private produtoService: ProdutoService,
    private route: ActivatedRoute
  ) {
    this.pedido = null
    this.pedidoUUID = null
    this.total = new BehaviorSubject<number>(0)
    this.totalFormatado = new BehaviorSubject<string>(
      this.toCurrencyString(this.total.value)
    )
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.pedidoUUID = params['pedidoID']
      if (!this.pedidoUUID) {
        let msg = 'ID do pedido nao encontrado!'
        alert(msg); throw new Error(msg)
      }
      this.pedidoService.getOne(this.pedidoUUID).subscribe({
        next: (response: any) => {
          this.pedido = {...response}
          this.fetchProducts()
        },
        error: (response) => {
          let msg = 'Erro na busca do pedido'
          alert(msg); console.log(response); throw new Error(msg)
        }
      })
    })
  }

  toCurrencyString(number: number): string {
    return `R$${Number(number).toFixed(2)}`.replace('.', ',')
  }

  fetchProducts() {
    if (!this.pedido) {
      let msg = 'Erro na requisição dos dados'
      alert(msg); throw new Error(msg)
    }
    for (let item of this.pedido.itens_pedido) {
      this.produtoService.getOne(item.produto_uuid).subscribe({
        next: (response) => {
          item.produto = response
          item.subtotal = `R$${Number(
            item.quantidade * item.produto.preco
          ).toFixed(2)}`.replace('.', ',')
          let totalAteAgora = this.total.getValue()
          totalAteAgora += Number(item.quantidade * item.produto.preco)
          this.total.next(totalAteAgora)
          this.totalFormatado.next(
            this.toCurrencyString(this.total.value)
          )
        },
        error: (response) => {
          console.log({response: response})
        }
      })
    }
  }

}
