from cryptography.fernet import Fernet
from config import settings as s


def criptografar(senha_original):
    senha_bytes = senha_original.encode('utf-8')
    chave = bytes(s.SECURITY_KEY, 'utf-8')
    f = Fernet(chave)
    senha_criptografada = f.encrypt(senha_bytes)
    return senha_criptografada


def descriptografar(senha_criptografada):

    chave = bytes(s.SECURITY_KEY, 'utf-8')
    f = Fernet(chave)
    senha_descriptografada = f.decrypt(senha_criptografada)
    senha_resultado = senha_descriptografada.decode('utf-8')
    return senha_resultado

