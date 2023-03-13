import jwt
import settings
import hashlib

password = hashlib.md5(b'1234').hexdigest()



def get_jwt_token(payload: dict = None):
    if payload is not None:
        return jwt.JWT().encode(payload, settings.KEY)

    raise "payload не соотвествует типу dict"