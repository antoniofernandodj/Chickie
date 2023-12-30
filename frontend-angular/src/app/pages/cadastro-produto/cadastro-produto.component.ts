import { Component } from '@angular/core';
import { ProdutoBodyRequest, ProdutoResponse } from '../../models/produto';
import { ActivatedRoute } from '@angular/router';
import { AuthData, AuthService } from '../../services/auth.service';
import { ProdutoService } from '../../services/produto.service';
import { CategoriaService } from '../../services/categoria.service';
import { CategoriaResponse, CategoriaBodyRequest } from '../../models/categoria';
import { BehaviorSubject } from 'rxjs';
import { FormsModule } from '@angular/forms';
import { Response201Wrapper } from '../../models/wrapper';

@Component({
  selector: 'app-cadastro-produto',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './cadastro-produto.component.html',
  styleUrl: './cadastro-produto.component.sass'
})
export class CadastroProdutoComponent {

  nomeValue: string
  descricaoValue: string
  precoValue: number | null
  categoriaValue: any

  companyProducts: BehaviorSubject<Array<ProdutoResponse>>
  companyCategorias: BehaviorSubject<Array<CategoriaResponse>>
  companyData: AuthData | null

  constructor(
    private produtoService: ProdutoService,
    private authService: AuthService,
    private categoriaService: CategoriaService
  ) {
    this.companyCategorias = new BehaviorSubject<Array<CategoriaResponse>>([])
    this.companyProducts = new BehaviorSubject<Array<ProdutoResponse>>([])
    this.companyData = this.authService.currentCompany()

    this.nomeValue = ''
    this.descricaoValue = ''
    this.precoValue = null
    this.categoriaValue = ''
  }

  fetchProducts() {
    if (!this.companyData) {
      let msg =' Dados da empresa não encontrados!'
      alert(msg); throw new Error(msg)
    }

    this.produtoService.getAll(this.companyData.uuid).subscribe({
      next: (res) => {
        if (Array.isArray(res)) {
          this.companyProducts.next(res)
          this.fetchCategoriasForProducts()
        }
      },
      error: (res) => { alert('Erro ao buscar pelos produtos') }
    })
  }

  fetchCategoriasForProducts() {
    for (let produto of this.companyProducts.value) {

      if (!this.companyData) {
        let msg =' Dados da empresa não encontrados!'
        alert(msg); throw new Error(msg)
      }

      this.categoriaService.getOne(produto.categoria_uuid).subscribe({
        next: (response) => {
          produto.categoria = response
        },
        error: (res) => { alert('Erro ao buscar pelas categorias') }
      })
    }

  }

  fetchCategorias() {
    if (!this.companyData) {
      alert('Dados da empresa não encontrados!')
      throw new Error('Dados da empresa não encontrados!')
    }
    this.categoriaService.getAll(this.companyData.uuid).subscribe({
      next: (response) => {
        if (Array.isArray(response)) {
          this.companyCategorias.next(response)
        }
      },
      error: (response) => {
        alert('Dados de categorias não encontrados!')
        throw new Error('Dados de categorias não encontrados!')
      },
    })
  }

  ngOnInit() {
    this.fetchCategorias()
    this.fetchProducts()
  }

  cadastrarProduto() {

    if (!this.companyData) {
      alert('Nenhuma empresa logada!')
      return
    }

    let inputs: Array<{ [key: string]: string | number | null }> = [
      {Nome: this.nomeValue},
      {Descricao: this.descricaoValue},
      {Preco: this.precoValue},
      {Categoria: this.categoriaValue}
    ]

    for (let inputData of inputs) {
      let title = Object.keys(inputData)[0];
      let element = inputData[title];

      if (element == null || element == undefined || element == '') {
        let msg = `O input ${title} é requerido!`;
        alert(msg); throw new Error(msg)
      }
    }

    let body = {
      loja_uuid: this.companyData.uuid,
      categoria_uuid: this.categoriaValue,
      nome: this.nomeValue,
      descricao: this.descricaoValue,
      preco: Number(this.precoValue || 0)
    }

    this.produtoService.save(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        alert('Item adicionado com sucesso!')
        this.categoriaService.getOne(this.categoriaValue).subscribe({
          next: (response) => {
            let newProduct = {...body, uuid: r.uuid, categoria: response}
            this.companyProducts.value.push(newProduct)
          }
        })
      },
      error: (response) => {
        let msg = 'Erro no cadastro do item';
        alert(msg); throw new Error(msg)
      }
    })

  }

}
