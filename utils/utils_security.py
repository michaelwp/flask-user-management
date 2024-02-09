from bcrypt import hashpw, checkpw, gensalt
from config import secret_key
import jwt


def generate_hash(password):
    try:
        pw = password.encode('utf-8')
        salt = gensalt(12)

        pw_hash = hashpw(pw, salt)
        return pw_hash, None
    except ValueError as err:
        return "", f"error generate hash: {err}"
    except:
        return "", "error generate hash"


def check_hash(password, pw_hash):
    try:
        pw = password.encode('utf-8')
        pwd_hash = pw_hash.encode('utf-8')

        is_match = checkpw(pw, pwd_hash)
        return is_match, None
    except ValueError as err:
        return False, f"error check hash: {err}"
    except:
        return False, "error check hash"


def generate_jwt_token(payload):
    try:
        token = jwt.encode(payload=payload, key=secret_key)
        return token, None
    except:
        return "", "error generate jwt token"


def decode_jwt_token(jwt_token):
    try:
        payload = jwt.decode(jwt=jwt_token, key=secret_key, verify=True, algorithms=["HS256"])
        return payload, None
    except jwt.ExpiredSignatureError as err:
        return "", f"error decode jwt token: {err}"
    except jwt.exceptions.DecodeError as err:
        return "", f"error decode jwt token: {err}"
    except:
        return "", "error decode jwt token"
