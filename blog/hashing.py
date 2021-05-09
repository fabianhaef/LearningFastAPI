from passlib.context import CryptContext

pwd_cxt = CryptContext(schememes=['bcrypt'], depracted="auto")

class Hash():
    def bcrypt(password: str):
        hashed_password = pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)