import axios from 'axios'
import { SyntheticEvent, useRef } from 'react'
import { useRouter } from 'next/router';



export default function Page() {

  let router = useRouter()
  let inputEmail = useRef<HTMLInputElement>(null);
  let inputPassword = useRef<HTMLInputElement>(null);

  const send = async (e: SyntheticEvent) => {
    e.preventDefault()
    if (inputEmail.current && inputPassword.current) {
      try {
        let data = {
          username: inputEmail.current.value,
          password: inputPassword.current.value
        }
        let response = await axios.post('/api/login', data)
        if (response.status == 200) {
          router.push(`/home/${response.data.uuid}`)
        }
      } catch (error) {
        console.log(error)
      }
    }
  }

  return (
    <main>
      <form onSubmit={send}>
        <div className="form-group">
          <div>
            <label htmlFor="login"></label>
          </div>
          <div>
            <input ref={inputEmail}
              id="login"
              name="login"
              type="text" />
          </div>
        </div>
        <div className="form-group">
          <div>
            <label htmlFor="login"></label>
          </div>
          <div>
            <input ref={inputPassword}
              id="password"
              type="password"
              name="password" />
          </div>
        </div>
        <div>
          <button>
            send
          </button>
        </div>
      </form>
    </main>
  )
}