export type IngredienteBodyRequest = {
  nome: string,
  loja_uuid: string
  produto_uuid: string
  descricao: string
}

export type Ingrediente = {
  nome: string,
  loja_uuid: string
  produto_uuid: string
  descricao: string,
  uuid: string,
}
