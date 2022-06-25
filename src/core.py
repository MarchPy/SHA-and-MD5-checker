import hashlib


def check(path, op):

    if op == '256':
        with open(path, 'rb') as file:
            byte = file.read()
            return hashlib.sha256(byte).hexdigest()

    elif op == '512':
        with open(path, 'rb') as file:
            byte = file.read()
            return hashlib.sha512(byte).hexdigest()

    elif op == 'md5':
        with open(path, 'rb') as file:
            byte = file.read()
            return hashlib.md5(byte).hexdigest()
