from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Gerando par de chaves RSA para os dois usuários
def gerar_chaves_rsa():
    # Gera uma chave privada RSA com tamanho de 2048 bits
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    # Obtém a chave pública correspondente à chave privada gerada
    chave_publica = chave_privada.public_key()
    return chave_privada, chave_publica

# Função para criptografar uma mensagem usando a chave pública
def criptografar_mensagem(chave_publica, mensagem):
    encrypted = chave_publica.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Função para descriptografar uma mensagem usando a chave privada
def descriptografar_mensagem(chave_privada, mensagem_criptografada):
    decrypted = chave_privada.decrypt(
        mensagem_criptografada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

# Simulação de comunicação entre dois usuários usando criptografia assimétrica
# Usuario A envia uma mensagem criptografada para Usuario B
print("Simulação de comunicação entre dois usuários usando criptografia assimétrica")

# Geração de chaves para os dois usuários
print("Gerando chaves RSA para os usuários A e B...")
chave_privada_A, chave_publica_A = gerar_chaves_rsa()
chave_privada_B, chave_publica_B = gerar_chaves_rsa()

# Usuario A envia uma mensagem para Usuario B
mensagem_A_para_B = "Olá, Usuario B! Esta é uma mensagem secreta."
print(f"Usuario A envia: {mensagem_A_para_B}")

# Criptografando a mensagem com a chave pública de Usuario B
mensagem_criptografada = criptografar_mensagem(chave_publica_B, mensagem_A_para_B)
print(f"Mensagem criptografada: {mensagem_criptografada}")

# Usuario B descriptografa a mensagem com sua chave privada
mensagem_descriptografada = descriptografar_mensagem(chave_privada_B, mensagem_criptografada)
print(f"Usuario B recebe: {mensagem_descriptografada}")