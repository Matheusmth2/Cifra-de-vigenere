import hashlib
import hmac
import os
import time

def generatehash(file_path: str, algorithm: str = "sha256") -> str:
    """
    Gera um hash HMAC de um arquivo usando o algoritmo especificado.
    """
    hash_func = getattr(hashlib, algorithm)
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_hash = hash_func(file_data).hexdigest()
    return file_hash

def verifyhash(download_path: str, expected_hash: str, algorithm: str = "sha256") -> bool:
    """
    Verifica se o hash HMAC de um arquivo corresponde ao hash esperado.
    """
    file_hash = generatehash(download_path, algorithm)
    print(f"Hash do arquivo: {file_hash}")
    print(f"Hash esperado: {expected_hash}")
    return file_hash == expected_hash

original_file = r"D:\USERS\Downloads\Cifra de vigenere\.env\Perfil.jpeg"
generated_hash_original = generatehash(original_file)
print(f"Hash gerado: {generated_hash_original}")

copia_file = r"D:\USERS\Downloads\Cifra de vigenere\.env\fundo.jpg"
if verifyhash(copia_file, generated_hash_original):
    print("O hash do arquivo copiado corresponde ao hash do arquivo original.")
else:
    print("O hash do arquivo copiado NÃO corresponde ao hash do arquivo original.")