import { Component } from '@angular/core';
import { FormsModule, FormBuilder, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { PrecoResponse, FileDataRequest, Ingrediente } from '../../../models/models';
import { CurrencyPipe } from '@angular/common';
import { SpinnerComponent } from '../../../components/spinner/spinner.component';

import {  AuthService, CompanyAuthData, ImageService,
          PrecoService, ProdutoService,
          IngredienteService } from '../../../services/services';

import { ButtonHandler } from '../../../handlers/button';


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
  imports: [
    FormsModule,
    RouterModule,
    CurrencyPipe,
    ReactiveFormsModule,
    SpinnerComponent
  ],
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
  ingredientes: BehaviorSubject<Array<Ingrediente>>

  selectedImage: string
  fileData: FileDataRequest
  atualizandoImagem: boolean

  nomeValue: string
  descricaoValue: string
  precoValue: number
  imageLoading: boolean
  nomeIngrediente: string
  descricaoIngrediente: string
  ingredientesLoading: boolean


  constructor(
    private formBuilder: FormBuilder,
    private precoService: PrecoService,
    private produtoService: ProdutoService,
    private route: ActivatedRoute,
    private authService: AuthService,
    private imageService: ImageService,
    private ingredienteService: IngredienteService,
  ) {
    this.imageLoading = false
    this.atualizandoImagem = false
    this.fileData = { bytes_base64: '', filename: '' }
    this.selectedImage = ''
    this.produto = new BehaviorSubject<Produto | null>(null)
    this.produtoUUID = ''
    this.diaDaSemanaValue = ''
    this.valorValue = null
    this.companyData = this.authService.currentCompany()
    this.imageForm = this.formBuilder.group({ imageFile: [''] })
    this.nomeIngrediente = ''
    this.descricaoIngrediente = ''
    this.ingredientesLoading = false

    this.nomeValue = ''
    this.descricaoValue = ''
    this.precoValue = 0

    this.diasDaSemanaCadastrados = new BehaviorSubject<Array<DiaSemana>>([])
    this.diasDaSemanaDisponiveis = new BehaviorSubject<Array<DiaSemana>>([])
    this.ingredientes = new BehaviorSubject<Array<Ingrediente>>([])
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.produtoUUID = params['id'];
    });
    this.refreshProdutoPrecos()
    this.refreshProdutoIngredientes()
  }

  async onFileSelected(event: any) {
    const file: File = event.target.files[0];
    if (file) {
      this.fileData.filename = file.name
      this.selectedImage = URL.createObjectURL(file)
      this.fileData.bytes_base64 = await this.imageService.getImageBytes(file)
    }
  }


  removeImage(event: Event) {
    let button = new ButtonHandler(event)
    button.disable('Removendo a imagem...')

    this.produtoService.removeImage(this.produtoUUID).subscribe({
      next: (result) => {
        alert('Imagem removida com sucesso!')
        this.fileData.filename = ''
        this.fileData.bytes_base64 = ''
        this.imageForm = this.formBuilder.group({ imageFile: [''] })
        this.refreshProdutoPrecos()
        button.enable()
      },
      error: (result) => {
        alert('Erro na remoção da imagem!')
        button.enable()
      }
    })
  }

  uploadImage(event: Event) {
    let button = new ButtonHandler(event)
    button.disable('Atualizando a imagem...')


    if (!this.fileData.bytes_base64) {
      button.enable()
      let msg = 'Selecione uma imagem!'
      alert(msg); throw new Error(msg)
    }
    this.produtoService.uploadImage(this.produtoUUID, this.fileData).subscribe({
      next: (result) => {
        button.enable()
        alert('Imagem atualizada com sucesso!')
      },
      error: (result) => {
        button.enable()
        alert('Erro na atualização da imagem!')
      }
    })
  }

  updateProdutoData(event: Event) {
    let button = new ButtonHandler(event)

    if (!this.companyData) {
      button.enable()
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
        button.enable()
        alert('Dados atualizados com sucesso!')

      },
      error: (result) => {
        button.enable()
        alert('Erro na atualização dos dados do produto!')

      }
    })
  }

  refreshProdutoPrecos() {
    this.imageLoading = true
    if (this.companyData) {
      this.produtoService.getOne(this.produtoUUID).subscribe({
        next: (result: any) => {
          this.imageLoading = false
          console.log({result: result})
          let produto = new Produto(result)
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
        error: (result) => {
          alert('Erro na busca pelo produto')
        }
      })
    }


  }

  refreshProdutoIngredientes() {
    this.ingredientesLoading = true
    this.ingredienteService.getAll(this.produtoUUID).subscribe({
      next: (result: any) => {
        this.ingredientes.next(result)
      },
      error: (result) => {
        console.error(result)
      }
    })
  }

  removerPreco(event: Event, preco: any) {
    let button  = new ButtonHandler(event)

    button.disable('Removendo...')

    this.precoService.delete(preco).subscribe({
      next: (response) => {
        button.enable()
        alert('Preço removido com sucesso!');
        this.refreshProdutoPrecos()
      },
      error: (response) => {
        button.enable()
        alert('Erro ao remover preço de produto')
      }
    })
  }

  removerIngrediente(event: Event, ingrediente: any) {
    let button  = new ButtonHandler(event)

    button.disable('Removendo...')

    this.ingredienteService.delete(ingrediente).subscribe({
      next: (response) => {
        button.enable()
        alert('Ingrediente removido com sucesso!');
        this.refreshProdutoIngredientes()
      },
      error: (response) => {
        button.enable()
        alert('Erro ao remover ingrediente de produto')
      }
    })
  }

  clearInputs() {
    this.valorValue = null
    this.diaDaSemanaValue = ''
    this.descricaoIngrediente = ''
    this.nomeIngrediente = ''
  }

  cadastrarPreco(event: Event) {
    let button = new ButtonHandler(event)
    button.disable('Salvando...')

    for (let input of [this.valorValue, this.diaDaSemanaValue]) {
      if (!input) {
        button.enable()
        let msg = 'É necessário preencher todos os campos!'
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
        button.enable()
        alert('Preço cadastrado com sucesso!')
        this.refreshProdutoPrecos()
        this.clearInputs()


      },
      error: (response) => {
        button.enable()
        alert('Erro no cadasto do preço')

      }
    })

  }

  cadastrarIngrediente(event: Event) {
    let button = new ButtonHandler(event)
    button.disable('Salvando...')

    for (let input of [this.nomeIngrediente, this.descricaoIngrediente]) {
      if (!input) {
        button.enable()
        let msg = 'É necessário preencher todos os campos!'
        alert(msg); throw new Error(msg)
      }
    }

    if (!this.companyData) {
      button.enable()
      let msg = 'Dados de loja não encontrados'
      alert(msg); throw new Error(msg)
    }

    let body = {
      nome: this.nomeIngrediente,
      descricao: this.descricaoIngrediente,
      produto_uuid: this.produtoUUID,
      loja_uuid: this.companyData.loja.uuid
    }

    this.ingredienteService.save(body).subscribe({
      next: (response) => {
        button.enable()
        alert('Ingrediente cadastrado com sucesso!')
        this.ngOnInit()
        this.clearInputs()
      },
      error: (response) => {
        button.enable()
        alert('Erro no cadasto do ingrediente')

      }
    })

  }
}
