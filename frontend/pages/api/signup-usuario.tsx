import axios from 'axios'
import { NextApiRequest, NextApiResponse } from 'next';


type SignUpRequestBody = {
  CEP: string
  UF: string
  cidade: string
  rua: string
  numero: string
  complemento: string
  bairro: string

  username: string
  password: string
  nome: string
  email: string
  telefone: string
  celular: string
}

interface SignUpRequest {
  method?: string
  body: SignUpRequestBody;
}

export default async function handler(
  request: NextApiRequest,
  response: NextApiResponse
) {

  const { method, body }: SignUpRequest = request;
  const { CEP, UF, cidade, rua,
          username, password, nome,
          email, telefone, celular,
          numero, complemento, bairro } = body

  if (method === 'POST') {

    let url1 = 'http://localhost:8000/endereco'
    
    let data1 = { CEP, UF, cidade, rua,
                  numero, complemento, bairro }
      
    let enderecoResponse = await axios.post(url1, data1)

    let url2 = 'http://localhost:8000/user/login'
    let data2 = { nome, username, email,
                  telefone, celular, password,
                  endereco_uuid: enderecoResponse.data.uuid }

    let signUpResponse = await axios.post(url2, data2)

    console.log(signUpResponse.data)

    response
      .status(200)
      .json(signUpResponse);

  } else {
    response.status(405).end();
  }
}
