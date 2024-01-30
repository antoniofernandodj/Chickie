import { Ingrediente } from "./ingrediente"


export type ProdutoBodyRequest = {
  loja_uuid: string,
  categoria_uuid: string,
  nome: string,
  preco: number,
  descricao: string,
  image_bytes: string
}

export type ProdutoPUTRequest = {
    nome: string,
    descricao: string,
    preco: number,
}

export type ProdutoResponse = {
  uuid: string
  loja_uuid: string,
  categoria_uuid: string,
  nome: string,
  preco: number,
  descricao: string,
  categoria?: any,
  ingredientes?: Array<Ingrediente>,
  image_url: string,
  preco_hoje?: number
}
