from src.api.security.company import current_company, authenticate_company
from src.api.security.user import current_user, authenticate_user
from src.api.security.scheme import oauth2_scheme
from src.api.security.token import create_access_token
import base64
import bcrypt


class HashService:

    @classmethod
    def hash(cls, password: str):
        salt = bcrypt.gensalt()
        hashpw = bcrypt.hashpw(password.encode("utf-8"), salt)
        hash_base64 = base64.b64encode(hashpw).decode("utf-8")
        return hash_base64