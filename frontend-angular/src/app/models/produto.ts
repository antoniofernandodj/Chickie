export type ProdutoBodyRequest = {
  loja_uuid: string,
  categoria_uuid: string,
  nome: string,
  preco: number,
  descricao: string
}

export type ProdutoResponse = {
  uuid: string
  loja_uuid: string,
  categoria_uuid: string,
  nome: string,
  preco: number,
  descricao: string,
  categoria?: any
}