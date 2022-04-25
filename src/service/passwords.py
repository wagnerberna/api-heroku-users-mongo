from src.static.message import ERROR_MESSAGE
from bcrypt import hashpw, checkpw, gensalt


def crypt_password(password):
    try:
        salt = gensalt()
        password_hashed = hashpw(password.encode("utf8"), salt)
        return password_hashed
    except Exception as error:
        print(ERROR_MESSAGE.format(error))


def compare_password(password, password_hashed):
    try:
        if checkpw(password.encode("utf8"), password_hashed.encode("utf8")):
            return True
        return False
    except Exception as error:
        print(ERROR_MESSAGE.format(error))
