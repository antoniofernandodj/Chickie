from dataclasses import dataclass
from typing import Union, Optional

from urllib.parse import parse_qs


class HTTPResponse:
    """Representação de uma resposta HTTP"""
    
    def __init__(
            self,
            status: Optional[str] = None,
            message: Optional[str] = None,
            status_code: Optional[int] = None,
            body: Optional[Union[str, dict]] = None,
            redirect: Optional[str] = None
        ):
        
        """
        Inicializa uma nova instância da classe HTTPResponse.

        Args:
            :param status (str): A mensagem de status HTTP, ex: 'OK'
            :param body (str | dict | None): O corpo da resposta HTTP, pode ser uma string, um dicionário ou None
            :param message (str | None): Mensagem opcional a ser incluída na resposta
            :param redirect (str | None): URL de Redirecionamento opcional a ser incluída na resposta
        """

        self.status = status
        self.body = body
        self.message = message
        self.redirect = redirect
        self.status_code = status_code
        
    def __repr__(self) -> str:
        return f'{type(self).__name__}(status={self.status})'
    
    def to_flask(self):
        """
        Converte a resposta HTTP em um objeto FlaskResponse.
        """
        from flask.wrappers import Response as FlaskResponse
        from flask import jsonify, make_response, redirect

        if self.redirect:
            response = make_response(redirect(self.redirect))

            if self.status_code:
                response.status_code = self.status_code

            return response
        
        if self.body is None:
            response = make_response(self.message)

            if self.status_code:
                response.status_code = self.status_code

            return response

        if isinstance(self.body, str):
            response = make_response(self.body)

            if self.status_code:
                response.status_code = self.status_code

            return response
        
        if isinstance(self.body, dict) or isinstance(self.body, list):
            response = jsonify(self.body)

            if self.status_code:
                response.status_code = self.status_code

            if not self.body:
                response.status_code = 404

            return response

