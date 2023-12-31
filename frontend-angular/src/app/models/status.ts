export type StatusBodyRequest = {
  loja_uuid: string,
  nome: string,
  descricao: string
}

export type StatusResponse = {
  uuid: string
  loja_uuid: string,
  nome: string,
  descricao: string
}
