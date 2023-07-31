import { useRef, SyntheticEvent } from "react"
import axios from 'axios'

export default function Page() {

    let inputNome = useRef<HTMLInputElement>(null)
    let inputUsername =  useRef<HTMLInputElement>(null)
    let inputSenha =  useRef<HTMLInputElement>(null)
    let inputEmail =  useRef<HTMLInputElement>(null)
    let inputTelefone =  useRef<HTMLInputElement>(null)
    let inputCelular =  useRef<HTMLInputElement>(null)
    let inputCEP =  useRef<HTMLInputElement>(null)
    let inputUF =  useRef<HTMLInputElement>(null)
    let inputCidade =  useRef<HTMLInputElement>(null)
    let inputRua =  useRef<HTMLInputElement>(null)
    let inputNumero =  useRef<HTMLInputElement>(null)
    let inputComplemento =  useRef<HTMLInputElement>(null)
    let inputBairro =  useRef<HTMLInputElement>(null)

    const submit = async (e: SyntheticEvent) => {

        e.preventDefault()
        if (
            inputNome.current &&
            inputUsername.current &&
            inputSenha.current &&
            inputEmail.current &&
            inputTelefone.current &&
            inputCelular.current &&
            inputCEP.current &&
            inputUF.current &&
            inputCidade.current &&
            inputRua.current &&
            inputNumero.current &&
            inputComplemento.current &&
            inputBairro.current
        ) {
            let url = '/api/signup/'
            let data = {
                nome: inputNome.current.value,
                username: inputUsername.current.value,
                password: inputSenha.current.value,
                email: inputEmail.current.value,
                telefone: inputTelefone.current.value,
                celular: inputCelular.current.value,
                CEP: inputCEP.current.value,
                UF: inputUF.current.value,
                cidade: inputCidade.current.value,
                rua: inputRua.current.value,
                numero: inputNumero.current.value,
                complemento: inputComplemento.current.value,
                bairro: inputBairro.current.value,
            }
            let response = await axios.post(url, data)
            if (response.status == 200) {
                console.log('Sucesso!')
            }

        }

    }

    return (
        <form onSubmit={submit}>
            <div>
                <div>
                    <label htmlFor="">Nome</label>
                </div>
                <div>
                    <input ref={inputNome}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">
                        Nome de usuário (login)
                    </label>
                </div>
                <div>
                    <input ref={inputUsername}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Senha</label>
                </div>
                <div>
                    <input ref={inputSenha}
                        type="password" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Email</label>
                </div>
                <div>
                    <input ref={inputEmail}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Telefone</label>
                </div>
                <div>
                    <input ref={inputTelefone}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Celular</label>
                </div>
                <div>
                    <input ref={inputCelular}
                        type="text" />
                </div>
            </div>

            <div>
                <div>
                    <label htmlFor="">CEP</label>
                </div>
                <div>
                    <input ref={inputCEP}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">UF</label>
                </div>
                <div>
                    <input ref={inputUF}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Cidade</label>
                </div>
                <div>
                    <input ref={inputCidade}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Rua</label>
                </div>
                <div>
                    <input ref={inputRua}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Numero</label>
                </div>
                <div>
                    <input ref={inputNumero}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Complemento</label>
                </div>
                <div>
                    <input ref={inputComplemento}
                        type="text" />
                </div>
            </div>
            <div>
                <div>
                    <label htmlFor="">Bairro</label>
                </div>
                <div>
                    <input ref={inputBairro}
                        type="text" />
                </div>
            </div>
            <div>
                <button>Cadastrar</button>
            </div>
        </form>
    )
}