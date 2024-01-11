import { Component } from '@angular/core';
import { FormsModule, FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { PrecoResponse, FileDataRequest } from '../../../models/models';
import { CurrencyPipe } from '@angular/common';

import {  AuthService, CompanyAuthData, ImageService,
          PrecoService, ProdutoService } from '../../../services/services';


class Produto {

  produto_uuid: string
  categoria_uuid: string
  descricao: string
  loja_uuid: string
  nome: string
  image_url?: string
  preco: number
  preco_hoje: number
  precos: Array<PrecoResponse>

  constructor(response: any) {
    this.produto_uuid = response.produto_uuid;
    this.categoria_uuid = response.categoria_uuid;
    this.descricao = response.descricao;
    this.loja_uuid = response.loja_uuid;
    this.nome = response.nome;
    this.preco = response.preco;
    this.preco_hoje = response.preco_hoje;
    this.precos = response.precos;
    this.image_url = response.image_url;
  }
}


type DiaSemana = {
  title: string;
  val: string;
}

let diasArray = [
  { title: 'Domingo', val: 'dom' },
  { title: 'Segunda', val: 'seg' },
  { title: 'Terça', val: 'ter' },
  { title: 'Quarta', val: 'qua' },
  { title: 'Quinta', val: 'qui' },
  { title: 'Sexta', val: 'sex' },
  { title: 'Sábado', val: 'sab' }
]

const getTitle = (dia: string) => {
  switch (dia) {
    case 'dom':
      return 'Domingo';
    case 'seg':
      return 'Segunda-feira';
    case 'ter':
      return 'Terça-feira';
    case 'qua':
      return 'Quarta-feira';
    case 'qui':
      return 'Quinta-feira';
    case 'sex':
      return 'Sexta-feira';
    case 'sab':
      return 'Sábado';
    default:
      return 'Dia inválido';
  }
};

@Component({
  selector: 'app-produto',
  standalone: true,
  imports: [FormsModule, RouterModule, CurrencyPipe, ReactiveFormsModule],
  templateUrl: './produto.component.html',
  styleUrl: './produto.component.sass'
})
export class ProdutoComponent {

  produtoUUID: string
  produto: BehaviorSubject<Produto | null>
  companyData: CompanyAuthData | null
  imageForm: FormGroup

  valorValue: number | null
  diaDaSemanaValue: string
  diasDaSemanaCadastrados: BehaviorSubject<Array<DiaSemana>>
  diasDaSemanaDisponiveis: BehaviorSubject<Array<DiaSemana>>

  selectedImage: string
  saving: boolean
  fileData: FileDataRequest
  atualizandoImagem: boolean

  nomeValue: string
  descricaoValue: string
  precoValue: number

  constructor(
    private formBuilder: FormBuilder,
    private precoService: PrecoService,
    private produtoService: ProdutoService,
    private route: ActivatedRoute,
    private authService: AuthService,
    private imageService: ImageService
  ) {
    this.atualizandoImagem = false
    this.fileData = { bytes_base64: '', filename: '' }
    this.selectedImage = ''
    this.saving = false
    this.produto = new BehaviorSubject<Produto | null>(null)
    this.produtoUUID = ''
    this.diaDaSemanaValue = ''
    this.valorValue = null
    this.companyData = this.authService.currentCompany()
    this.imageForm = this.formBuilder.group({ imageFile: [''] })

    this.nomeValue = ''
    this.descricaoValue = ''
    this.precoValue = 0

    this.diasDaSemanaCadastrados = new BehaviorSubject<Array<DiaSemana>>([])
    this.diasDaSemanaDisponiveis = new BehaviorSubject<Array<DiaSemana>>([])
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.produtoUUID = params['id'];
    });
    this.refreshProdutoPrecos()
  }

  async onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.fileData.filename = file.name
      this.selectedImage = URL.createObjectURL(file)
      this.fileData.bytes_base64 = await this.imageService.getImageBytes(file)
    }
  }


  removeImage() {
    this.produtoService.removeImage(this.produtoUUID).subscribe({
      next: (result) => {
        alert('Imagem removida com sucesso!')
        this.fileData.filename = ''
        this.fileData.bytes_base64 = ''
        this.imageForm = this.formBuilder.group({ imageFile: [''] })
        this.refreshProdutoPrecos()
      },
      error: (result) => {
        alert('Erro na remoção da imagem!')
      }
    })
  }

  uploadImage() {
    if (!this.fileData.bytes_base64) {
      let msg = 'Selecione uma imagem!'
      alert(msg); throw new Error(msg)
    }
    this.produtoService.uploadImage(this.produtoUUID, this.fileData).subscribe({
      next: (result) => {
        alert('Imagem atualizada com sucesso!')
      },
      error: (result) => {
        alert('Erro na atualização da imagem!')
      }
    })
  }

  updateProdutoData(event: Event) {
    let button = event.target as HTMLButtonElement

    button.disabled = true
    button.innerHTML = 'Atualizando os dados...'

    if (!this.companyData) {
      let msg = 'Não deu';
      alert(msg); throw new Error()
    }

    let body = {
      nome: this.nomeValue,
      descricao: this.descricaoValue,
      preco: this.precoValue,
    }
    this.produtoService.update(this.produtoUUID, body).subscribe({
      next: (result) => {
        alert('Dados atualizados com sucesso!')

        button.disabled = false
        button.innerHTML = 'Atualizar dados'

      },
      error: (result) => {
        alert('Erro na atualização dos dados do produto!')

        button.disabled = false
        button.innerHTML = 'Atualizar dados'

      }
    })
  }

  refreshProdutoPrecos() {

    if (this.companyData) {
      this.produtoService.getOne(this.produtoUUID).subscribe({
        next: (response) => {
          console.log({response: response})
          let produto = new Produto(response)
          this.produto.next(produto)

          this.nomeValue = produto.nome
          this.precoValue = produto.preco
          this.descricaoValue = produto.descricao

          let diasDaSemanaCadastrados = produto.precos.map(preco => ({
              val: preco.dia_da_semana,
              title: getTitle(preco.dia_da_semana)
          }))

          this.diasDaSemanaCadastrados.next(diasDaSemanaCadastrados)
          const arrayDiasCadastrados = diasDaSemanaCadastrados.map(i => i.val)

          this.diasDaSemanaDisponiveis.next([])
          let newArr = []
          for (let dia of diasArray) {
            if (!arrayDiasCadastrados.includes(dia.val)) {
              newArr.push(dia)
            }
          }
          this.diasDaSemanaDisponiveis.next(newArr)
        },
        error: (response) => {
          alert('Erro na busca pelo produto')
        }
      })
    }


  }

  removerPreco(event: Event, preco: any) {
    let button  = event.target as HTMLButtonElement

    let initialHTML = button.innerHTML

    button.innerHTML = 'Removendo...'
    button.disabled = true

    this.precoService.delete(preco).subscribe({
      next: (response) => {
        alert('Preço removido com sucesso!');
        this.refreshProdutoPrecos()
      },
      error: (response) => {
        button.innerHTML = initialHTML
        button.disabled = false
        alert('Erro ao remover preço de produto')
      }
    })
  }

  clearInputs() {
    this.valorValue = null
    this.diaDaSemanaValue = ''
    this.saving = false
  }

  cadastrarPreco(event: Event) {

    let button = event.target as HTMLButtonElement

    button.disabled = true
    button.innerHTML = 'Salvando...'

    this.saving = true
    for (let input of [this.valorValue, this.diaDaSemanaValue]) {
      if (!input) {
        let msg = 'É necessário preencher todos os campos!'
        this.saving = false
        alert(msg); throw new Error(msg)
      }
    }

    let body = {
      valor: this.valorValue || 0,
      dia_da_semana: this.diaDaSemanaValue,
      produto_uuid: this.produtoUUID
    }

    this.precoService.save(body).subscribe({
      next: (response) => {
        alert('Preço cadastrado com sucesso!')
        this.refreshProdutoPrecos()
        this.clearInputs()

        button.disabled = true
        button.innerHTML = 'Salvar'

      },
      error: (response) => {
        this.saving = false
        alert('Erro no cadasto do preço')

        button.disabled = true
        button.innerHTML = 'Salvar'

      }
    })

  }
}
