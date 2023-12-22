'use client'
import Image from 'next/image'
import axios from 'axios'


export async function getData() {

  let formData = new FormData();
  formData.append('username', 'jose');
  formData.append('password', '123123');

  let config = {
    headers: { 'Content-Type': 'multipart/form-data' }
  };
  let url = 'http://localhost:8000/user/login'
  let response = await axios.post(url, formData, config)
  console.log(response)

}

export default function Home() {

  return (
    <div>
      <div>
        <input type="text" id="username"/>
      </div>
      <div>
        <input type="password" id="password"/>
      </div>
      <div>
        <button onClick={getData}>login</button>
      </div>
    </div>
  )
}

