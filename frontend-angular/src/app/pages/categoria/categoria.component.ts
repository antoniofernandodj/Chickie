import { Component } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { ProdutoService } from '../../services/produto.service';
import { AuthService, AuthData } from '../../services/auth.service';
import { CommonModule } from '@angular/common';
import { ProdutoResponse } from '../../models/produto';
import { BehaviorSubject } from 'rxjs';
import { Response201Wrapper } from '../../models/wrapper';
import { FormsModule } from '@angular/forms';


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
  companyData: AuthData | null

  nomeValue: string
  descricaoValue: string
  precoValue: number | null

  constructor(
    private route: ActivatedRoute,
    private produtoService: ProdutoService,
    private authService: AuthService
  ) {
    this.companyProducts = new BehaviorSubject<Array<ProdutoResponse>>([])
    this.companyData = this.authService.currentCompany();
    this.categoriaUUID = '';

    this.nomeValue = '';
    this.descricaoValue = '';
    this.precoValue = null
  }

  fetchProducts() {
    if (!this.companyData) {
      let msg = "Erro ao buscar dados da loja!"
      alert(msg); throw new Error(msg)
    }

    this.produtoService.getAll(this.companyData.uuid, this.categoriaUUID).subscribe({
      next: (response) => {
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
      alert('Nenhuma empresa logada!');
      throw new Error(JSON.stringify('Nenhuma empresa logada!'))
    }

    let body = {
      loja_uuid: this.companyData.uuid,
      categoria_uuid: this.categoriaUUID,
      nome: this.nomeValue,
      descricao: this.descricaoValue,
      preco: this.precoValue || 0
    }

    this.produtoService.save(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        this.companyProducts.value.push({...body, uuid: r.uuid});
        alert('Item adicionado com sucesso!');
      },
      error: (response) => {
        alert('Erro no cadastro do item');
      }
    })

  }
}
