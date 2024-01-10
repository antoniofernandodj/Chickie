import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BehaviorSubject } from 'rxjs';
import { FormsModule, FormBuilder, FormGroup } from '@angular/forms';

import {  ProdutoResponse, Response201ImageCreatedWrapper,
          FileDataRequest } from '../../../models/models';

import {  AuthService, CompanyAuthData, ProdutoService,
          ImageService, LojaService } from '../../../services/services';


@Component({
  selector: 'app-categoria',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule],
  templateUrl: './categoria.component.html',
  styleUrl: './categoria.component.sass'
})
export class CategoriaComponent {
  categoriaUUID: string
  companyProducts: BehaviorSubject<Array<ProdutoResponse>>
  companyData: CompanyAuthData | null

  nomeValue: string
  descricaoValue: string
  precoValue: number | null
  imageForm: FormGroup
  file: FileDataRequest | null
  selectedImage = ''
  loading: boolean

  constructor(
    private route: ActivatedRoute,
    private produtoService: ProdutoService,
    private authService: AuthService,
    private formBuilder: FormBuilder,
    private imageService: ImageService,
    private lojaService: LojaService
  ) {
    this.loading = false
    this.companyProducts = new BehaviorSubject<Array<ProdutoResponse>>([])
    this.categoriaUUID = '';
    this.companyData = null
    this.nomeValue = '';
    this.descricaoValue = '';
    this.precoValue = null;
    this.file = null;
    this.imageForm = this.formBuilder.group({ imageFile: [''] });
    this.selectedImage = ''
  }

  fetchProducts() {
    if (!this.companyData) {
      let msg = "Erro ao buscar dados da loja!";
      alert(msg); throw new Error(msg);
    }
    this.loading = true
    this.lojaService.getAllProducts(
      this.companyData.loja.uuid,
      this.categoriaUUID
    ).subscribe({
      next: (response) => {
        this.loading = false
        if (Array.isArray(response)) {
          this.companyProducts.next(response);
        }
      },
      error: (response) => {
        alert('Erro ao buscar pelos produtos')
        throw new Error(JSON.stringify(response))
      }
    })
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.categoriaUUID = params['id'];
      this.companyData = this.authService.currentCompany();
      this.fetchProducts()
    });
  }

  removerProduto(produto: ProdutoResponse) {
    this.produtoService.delete(produto).subscribe({
      next: (response) => {
        alert('Produto removido com sucesso!');
        let newArr = this.companyProducts.getValue();
        newArr = newArr.filter((p: ProdutoResponse) => p.uuid != produto.uuid);
        this.companyProducts.next(newArr)
      },
      error: (response) => {
        alert("Erro na remoção do produto");
        throw new Error(JSON.stringify(response))
      }
    })
  }

  cadastrarProduto() {
    if (!this.companyData) {
      let msg = 'Nenhuma empresa logada!'
      alert(msg); throw new Error(msg)
    }

    if (
      this.file == null ||
      this.file.bytes_base64 === "" ||
      this.file.bytes_base64 === null
    ) {
      let msg = 'Nenhuma imagem selecionada!'
      alert(msg); throw new Error(msg)
    }

    let body = {
      loja_uuid: this.companyData.loja.uuid,
      categoria_uuid: this.categoriaUUID,
      nome: this.nomeValue,
      descricao: this.descricaoValue,
      preco: Number(this.precoValue || 0),
      image_bytes: this.file.bytes_base64.split(',')[1],
      filename: this.file.filename
    }


    this.produtoService.save(body).subscribe({
      next: (response) => {
        let r = new Response201ImageCreatedWrapper(response)

        let newItem = {
          uuid: r.uuid,
          image_url: r.image_url,
          loja_uuid: body.loja_uuid,
          categoria_uuid: body.categoria_uuid,
          nome: body.nome,
          descricao: body.descricao,
          preco: body.preco,
        }

        this.companyProducts.value.push(newItem);
        alert('Item adicionado com sucesso!');
        this.clearInputs()
      },
      error: (response) => {
        console.log({response: response})
        alert('Erro no cadastro do item');
      }
    })

  }

  clearInputs() {
    this.nomeValue = '';
    this.descricaoValue = '';
    this.precoValue = null;
    this.file = null;
    this.selectedImage = ''
    let fileInput = document.querySelector('file-input') as HTMLInputElement
    if (fileInput){
      fileInput.value = ''
    }
  }

  async onFileSelected(event: any) {
    const eventFile: File = event.target.files[0];
    if (eventFile) {
      this.selectedImage = URL.createObjectURL(eventFile)
      this.file = {
        filename: eventFile.name,
        bytes_base64: await this.imageService.getImageBytes(eventFile)

      }
      console.log(this.file)
    }
  }
}
