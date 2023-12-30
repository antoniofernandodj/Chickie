export type PrecoBodyRequest = {
  dia_da_semana: string,
  produto_uuid: string,
  valor: number
}

export type PrecoResponse = {
  uuid: string
  dia_da_semana: string,
  produto_uuid: string,
  valor: number
}
