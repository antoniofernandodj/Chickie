import { Component } from '@angular/core';
import { PrecoService } from '../../services/preco.service';
import { ActivatedRoute } from '@angular/router';
import { AuthService, AuthData } from '../../services/auth.service';
import { BehaviorSubject } from 'rxjs';
import { Response201Wrapper } from '../../models/wrapper';
import { FormsModule } from '@angular/forms';
import { ProdutoService } from '../../services/produto.service';
import { ProdutoResponse } from '../../models/produto';

type DiaSemana = {
  title: string;
  val: string;
}

@Component({
  selector: 'app-produto',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './produto.component.html',
  styleUrl: './produto.component.sass'
})
export class ProdutoComponent {

  produtoUUID: string
  produto: ProdutoResponse | any
  companyData: AuthData | null
  produtoPrecos: BehaviorSubject<Array<any>>
  valorValue: number | null
  diaDaSemanaValue: string
  diasDaSemanaCadastrados: BehaviorSubject<Array<string>>
  diasDaSemanaDisponiveis: BehaviorSubject<Array<DiaSemana>>

  constructor(
    private precoService: PrecoService,
    private produtoService: ProdutoService,
    private route: ActivatedRoute,
    private authService: AuthService
  ) {
    this.produto = null
    this.produtoUUID = ''
    this.diaDaSemanaValue = ''
    this.valorValue = null
    this.companyData = this.authService.currentCompany()
    this.produtoPrecos = new BehaviorSubject<Array<any>>([])
    this.diasDaSemanaCadastrados = new BehaviorSubject<Array<string>>([])
    this.diasDaSemanaDisponiveis = new BehaviorSubject<Array<DiaSemana>>([
      { title: 'Domingo', val: 'dom' },
      { title: 'Segunda', val: 'seg' },
      { title: 'Terça', val: 'ter' },
      { title: 'Quarta', val: 'qua' },
      { title: 'Quinta', val: 'qui' },
      { title: 'Sexta', val: 'sex' },
      { title: 'Sábado', val: 'sab' }
    ])
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.produtoUUID = params['id'];
    });

    if (this.companyData) {

      this.precoService.getAll(this.produtoUUID).subscribe({
        next: (response) => {
          if (Array.isArray(response)) {
            let diasDaSemana = response.map(i => i.dia_da_semana)
            this.diasDaSemanaCadastrados.next(diasDaSemana)
            let diasDaSemanaDisponiveis = this.diasDaSemanaDisponiveis.getValue()
            diasDaSemanaDisponiveis = diasDaSemanaDisponiveis.filter(
              d => !this.diasDaSemanaCadastrados.value.includes(d.val)
            )
            this.produtoPrecos.next(response)
            this.diasDaSemanaDisponiveis.next(diasDaSemanaDisponiveis)
          }
        },
        error: (response) => {
          alert('Erro na busca pelos preços')
        }
      })

      this.produtoService.getOne(this.produtoUUID).subscribe({
        next: (response) => {
          this.produto = response
        },
        error: (response) => {
          alert('Erro na busca pelo produto')
        }
      })
    }
  }

  removerPreco(preco: any) {
    this.precoService.delete(preco).subscribe({
      next: (response) => {
        alert('Preço removido com sucesso!');
        let newArr = this.produtoPrecos.getValue()
          .filter(i => i.uuid != preco.uuid)

        this.produtoPrecos.next(newArr)

        this.updateDiasDaSemanaCadastradosRemove(preco.dia_da_semana)
        this.updateDiasDaSemanaDisponiveis()
      },
      error: (response) => {
        alert('Erro ao remover preço de produto')
      }
    })
  }

  updateDiasDaSemanaDisponiveis() {
    let diasDaSemanaDisponiveis = this.diasDaSemanaDisponiveis.getValue()
    diasDaSemanaDisponiveis = diasDaSemanaDisponiveis.filter(
      dia => !this.diasDaSemanaCadastrados.value.includes(dia.val)
    )
    this.diasDaSemanaDisponiveis.next(diasDaSemanaDisponiveis)
  }

  updateDiasDaSemanaCadastradosAdd(dia: string) {
    let diasDaSemanaCadastrados = this.diasDaSemanaCadastrados.getValue()
    this.diasDaSemanaCadastrados.next(
      [...diasDaSemanaCadastrados, dia]
    )
  }

  updateDiasDaSemanaCadastradosRemove(dia: string) {
    let newDiasDaSemanaCadastrados = this.diasDaSemanaCadastrados.getValue()
    newDiasDaSemanaCadastrados = newDiasDaSemanaCadastrados
      .filter(item => item != dia)

    this.diasDaSemanaCadastrados.next(newDiasDaSemanaCadastrados)
  }

  cadastrarPreco() {
    let inputs = [this.valorValue, this.diaDaSemanaValue]
    for (let input of inputs) {
      if (!input) {
        alert('É necessário preencher todos os campos!')
        throw new Error('É necessário preencher todos os campos!')
      }
    }

    let body = {
      'valor': this.valorValue || 0,
      'dia_da_semana': this.diaDaSemanaValue,
      'produto_uuid': this.produtoUUID
    }


    this.precoService.save(body).subscribe({
      next: (response) => {
        let r = new Response201Wrapper(response)
        this.produtoPrecos.value.push({...body, uuid: r.uuid})
        alert('Preço cadastrado com sucesso!')
        this.updateDiasDaSemanaCadastradosAdd(this.diaDaSemanaValue)
        this.updateDiasDaSemanaDisponiveis()

        this.valorValue = null
        this.diaDaSemanaValue = ''
      },
      error: (response) => {
        alert('Erro no cadasto do preço')
      }
    })

  }
}
