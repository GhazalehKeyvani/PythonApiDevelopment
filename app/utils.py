from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # hash_password = pwb_context.hash(**user.dict())
    # user.password = hash_password


def hash_password(password: str):
    return pwd_context.hash(password)
 
def verify(plain_password , hash_password):

    return pwd_context.verify(plain_password, hash_password)