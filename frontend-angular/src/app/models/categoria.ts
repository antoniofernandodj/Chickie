export type CategoriaBodyRequest = {
  descricao: string,
  loja_uuid: string,
  nome: string
}

export type CategoriaResponse = {
  uuid: string
  descricao: string,
  loja_uuid: string,
  nome: string
}
