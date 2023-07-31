import axios from 'axios'
import { NextApiRequest, NextApiResponse } from 'next';

type SignUpEmpresaResponse = {

}

export default async function handler(
	request: NextApiRequest,
	response: NextApiResponse
) {
	const { method, body } = request;

	if (method === 'POST') {
		let form = new FormData()
		form.append('username', body.username)
		form.append('password', body.password)
		let url = 'http://localhost:8000/user/login'
		let request = await axios.post(url, form, {
			headers: {
				'content-type': 'multipart/form-data'
			}
		})

		console.log(request.data)

		let loginData: SignUpEmpresaResponse = request.data

		response
			.status(200)
			.json(loginData);

	} else {
		response.status(405).end();
	}
}