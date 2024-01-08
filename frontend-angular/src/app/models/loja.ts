import { Endereco } from "./endereco"

export type LojaResponse = {
  celular: string,
  imagem_cadastro: string | null;
  email: string,
  endereco_uuid: string
  nome: string,
  telefone: string,
  username: string,
  endereco: Endereco;
  uuid: string,
  frete: number
}
