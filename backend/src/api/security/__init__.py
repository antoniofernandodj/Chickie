from src.api.security.company import current_company, authenticate_company
from src.api.security.user import current_user, authenticate_user
from src.api.security.scheme import oauth2_scheme
from src.api.security.token import create_access_token
from src.api.security.auth_service import AuthService  # noqa
import base64
import bcrypt

from src.api.security.hash_service import HashService  # noqa