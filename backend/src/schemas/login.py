from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    password: str
    email: Optional[str] = None
    username: Optional[str] = None

    # class Config:
    #     schema_extra = {
    #         'example': {

    #         }
    #     }
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'password': 'minha_senha',
                    'email': 'user123@email.com',
                },
                {
                    'password': 'minha_senha',
                    'username': 'user123',
                }
            ]
        }
    }
