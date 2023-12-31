import { Component } from '@angular/core';
import { LojaService } from '../../services/loja.service';
import { ActivatedRoute } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';
import { ProdutoService } from '../../services/produto.service';
import { ProdutoResponse } from '../../models/produto';
import { CategoriaResponse } from '../../models/categoria';
import { AuthData, AuthService } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';
import { CategoriaService } from '../../services/categoria.service';
import { FormsModule } from '@angular/forms';
import { v4 as uuidv4 } from 'uuid';
import { PedidoService } from '../../services/pedido.service';
import { NgxMaskDirective } from 'ngx-mask';




export type LojaResponse = {
  celular: string,
  email: string,
  endereco_uuid: string
  nome: string,
  telefone: string,
  username: string,
  uuid: string,
  frete: number
}

export type Endereco = {
  uf: string,
  cidade: string,
  logradouro: string,
  numero: string,
  bairro: string,
  cep: string,
  complemento: string,
}

export type ItemPedido = {
  produto: string,
  quantidade: number
  uuid: string
}

@Component({
  selector: 'app-loja',
  standalone: true,
  imports: [FormsModule, NgxMaskDirective],
  templateUrl: './loja.component.html',
  styleUrl: './loja.component.sass'
})
export class LojaComponent {

  loja: LojaResponse | null
  companyProducts: BehaviorSubject<Array<ProdutoResponse>>
  companyData: AuthData | null
  companyCategorias: BehaviorSubject<Array<CategoriaResponse>>
  produtoValue: any
  numeroDeItens: BehaviorSubject<Array<ItemPedido>>
  userData: any
  endereco: Endereco
  celular: string

  constructor(
    private route: ActivatedRoute,
    private produtoService: ProdutoService,
    private categoriaService: CategoriaService,
    private lojaService: LojaService,
    private authService: AuthService,
    private pedidoService: PedidoService

  ) {
    this.userData = null
    this.loja = null
    this.companyData = null
    this.produtoValue = null
    this.companyProducts = new BehaviorSubject<Array<ProdutoResponse>>([]);
    this.companyCategorias = new BehaviorSubject<Array<CategoriaResponse>>([]);
    this.numeroDeItens = new BehaviorSubject<Array<ItemPedido>>(
      [{ quantidade: 1, produto: '', uuid: uuidv4()}]
    );
    this.celular = ''
    this.endereco = {
      uf: '',
      cidade: '',
      logradouro: '',
      numero: '',
      bairro: '',
      cep: '',
      complemento: '',
    }
  }

  ngOnInit(): void {
    this.userData = this.authService.currentUser()
    this.celular = this.userData.celular
    if (this.userData?.endereco) {
      this.endereco = this.userData.endereco
    }
    this.route.params.subscribe(params => {
      let loja_uuid = params['lojaID'];
      this.fetchLoja(loja_uuid);
      this.fetchProducts(loja_uuid)
    })
  }

  addItem() {
    const randomUUID: string = uuidv4();
    this.numeroDeItens.value.push({ quantidade: 1, produto: '', uuid: randomUUID})
  }

  removeItem(item: any) {

    if (!(this.numeroDeItens.value.length > 1)) {
      throw new Error('O pedido necessita de ao menos um pedido!')
    }

    let newArr = this.numeroDeItens.getValue()
    newArr = newArr.filter(u => item.uuid != u.uuid)
    this.numeroDeItens.next(newArr)
  }

  private fetchLoja(companyUUID: string): void {
    this.lojaService.getOne(companyUUID).subscribe({
      next: (response: any) => {
        this.loja = {...response};
      },
      error: (response: HttpErrorResponse) => {
        let msg = '132: Erro na requisição dos dados da loja!';
        alert(msg); throw new Error(msg);
      }
    })
  }

  fetchProducts(companyUUID: string) {
    this.produtoService.getAll(companyUUID).subscribe({
      next: (res) => {
        if (Array.isArray(res)) {
          this.companyProducts.next(res)
          this.fetchCategoriasForProducts()
        }
      },
      error: (response: HttpErrorResponse) => {
        let msg = '148: Erro ao buscar pelos produtos'
        alert(msg); throw new Error(msg)
      }
    })
  }

  fetchCategoriasForProducts() {
    for (let produto of this.companyProducts.value) {

      this.categoriaService.getOne(produto.categoria_uuid).subscribe({
        next: (response) => {
          produto.categoria = response
        },
        error: (response: HttpErrorResponse) => {
          let msg = '162: Erro ao buscar pelas categorias'
          alert(msg); throw new Error(msg)
        }
      })

    }

  }

  cadastrarProduto() {
    let numeroCelular = this.celular.replace(/\D/g, '');
    if (numeroCelular.length != 11) {
      alert('O numero de celular precisa ter 11 digitos contando com o DDD!')
      return
    }

    let user = this.authService.currentUser()
    if (!this.loja) {
      return
    }

    let itens = this.numeroDeItens.getValue()
    for (let item of itens) {
      if (!item.produto) {
        alert('O campo produto é obrigatório!')
        return
      }
    }

    let body = {
      celular: numeroCelular,
      data_hora: new Date().toISOString(),
      endereco: this.endereco,
      frete: this.loja.frete || 0,
      itens_pedido: itens.map(item => ({
        produto_uuid: item.produto,
        quantidade: item.quantidade
      })),
      loja_uuid: this.loja.uuid,
      status_uuid: null,
      usuario_uuid: null
    }

    if (this.userData) {
      body.usuario_uuid = this.userData.uuid
    }

    this.pedidoService.save(body).subscribe({
      next: (response) => {
        console.log({response: response})
        alert('Pedido Cadastrado com sucesso!')
      },
      error: (response) => {
        console.log({response: response})
        alert('Erro no cadastro dos produtos')
      }
    })
  }
}
