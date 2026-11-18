#Importa a biblioteca nativa do Python chamada hashlib, que fornece vários algoritmos de criptografia e resumo de dados seguros (como MD5, SHA-1, SHA-256, etc.).
import hashlib
# Cria uma função reutilizável chamada criar_hash_sha256 que aceita dois parâmetros: o usuário e a senha.
def criar_hash_sha256(user, senha):
    #Junta o usuário e a senha usando um separador de dois-pontos (ex: admin:123456).
    #O método .encode('utf-8') converte essa string de texto em uma sequência de bytes, que é o formato exigido pelas funções matemáticas da biblioteca hashlib.
    senha_codificada = f"{user}:{senha}".encode('utf-8')
    #Inicializa o algoritmo SHA-256 passando os bytes combinados. O SHA-256 gera sempre uma saída única de tamanho fixo (256 bits, ou 32 bytes) para qualquer entrada.
    hash_object = hashlib.sha256(senha_codificada)
    #Converte o resultado binário do hash em uma string em formato hexadecimal (uma sequência legível de 64 caracteres contendo letras de a a f e números de 0 a 9).
    hash_hex = hash_object.hexdigest()
    return hash_hex

user = "admin"
senha = "123456"
hash_hex = criar_hash_sha256(user, senha)
print(f"Hash SHA-256 para {user}:{senha} é: {hash_hex}")