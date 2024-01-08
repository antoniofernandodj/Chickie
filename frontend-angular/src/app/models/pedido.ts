export type Pedido = {
  celular: string;
  data_hora: string;
  endereco_uuid: string | null;
  endereco: {
    bairro: string;
    cep: string,
    cidade: string;
    uf: string;
    logradouro: string;
    numero: string;
    complemento: string;
    uuid: string
  };
  status: any;
  frete: number;
  itens: Array<{
    loja_uuid: string;
    pedido_uuid: string;
    produto_uuid: string;
    produto_nome: string;
    produto_descricao: string;
    subtotal: number;
    quantidade: number;
    valor: number,
    uuid: string;
  }>;
  loja_uuid: string;
  status_uuid: string | null;
  total: number
  uuid: string;
};

