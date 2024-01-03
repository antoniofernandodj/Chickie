import { Component } from '@angular/core';
import { CategoriaService } from '../../services/categoria.service';
import { CategoriaBodyRequest, CategoriaResponse } from '../../models/categoria';
import { CompanyAuthData, AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { Response201Wrapper } from '../../models/wrapper';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-cadastro-categoria',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './cadastro-categoria.component.html',
  styleUrl: './cadastro-categoria.component.sass'
})
export class CadastroCategoriaComponent {

  companyData: CompanyAuthData | null
  categorias: BehaviorSubject<Array<CategoriaResponse>>
  descricaoValue: string
  nomeValue: string

  constructor (private service: CategoriaService, authService: AuthService) {
    this.descricaoValue = ''
    this.nomeValue = ''
    this.companyData = authService.currentCompany()
    this.categorias = new BehaviorSubject<Array<CategoriaResponse>>([])
  }

  ngOnInit() {
    if (this.companyData) {
      console.log(this.companyData)
      this.service.getAll(this.companyData.loja.uuid).subscribe({
        next: (response: Object) => {
          if (Array.isArray(response)) {
            this.categorias.next(response)
          }
        },
        error: (response: Object) => {
          throw new Error(JSON.stringify(response))
        }
      })
    }
  }

  registerCategoria() {
    if (!this.companyData) {
      alert('Nenhuma empresa logada!')
      throw new Error('Nenhuma empresa logada!')
    }

    let body = {
      descricao: this.descricaoValue,
      loja_uuid: this.companyData.loja.uuid,
      nome: this.nomeValue
    }

    this.service.save(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        alert('Item salvo com sucesso!');
        this.categorias.value.push({...body, uuid: r.uuid})
      },
      error: (response) => {
        alert('Erro no registro da categoria');
        throw new Error(JSON.stringify(response))
      }
    })
  }


  deleteCategoria(categoria: CategoriaResponse) {
    this.service.delete(categoria).subscribe({
      next: (response: Object) => {
        let newArray = this.categorias.getValue()
        .filter(i => i.uuid != categoria.uuid)

        this.categorias.next(newArray)
        alert('Item removido');
      },
      error: (response: Object) => {
        alert('Erro na remoção da categoria');
        throw new Error(JSON.stringify(response))
      }
    })
  }


}
