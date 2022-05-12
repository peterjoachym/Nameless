from cryptography.fernet import Fernet


salt = b'mL0GMACTOB-x8Qbs7pd1dFgivqkpOeZeypk-PWDPDKk='
fernet = Fernet(salt)


def encrypt_filename(filename: str):
    """encrypt filename"""
    token = fernet.encrypt(filename.encode())
    return token

def decrypt_filename(token : bytes):
    """decrypt filename"""
    filename = fernet.decrypt(token).decode()
    return filename

