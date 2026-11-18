import jwt
from datetime import datetime, timedelta, timezone

def gerar_jwt(usuario, nome, is_admin):
    """
    Gera um token JWT para o usuário fornecido.

    Args:
        usuario (str): O nome de usuário.
        nome (str): O nome completo do usuário.
        is_admin (bool): Indica se o usuário é administrador.
        exp (datetime): A data de expiração do token.
        iat (datetime): A data de emissão do token.

    Returns:
        str: O token JWT gerado.
    """

    # Defina a chave secreta para assinar o token
    secret_key = "sua_chave_secreta"

    # Defina o payload do token
    payload = {
        "usuario": usuario,
        "nome": nome,
        "is_admin": is_admin,
        "exp": datetime.now(timezone.utc)+ timedelta(hours=1),  # Token expira em 1 hora
        "iat": datetime.now(timezone.utc)  # Data de emissão do token
    }

    # Gere o token JWT
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token
print("Gerando token JWT para o usuário 'usuario_exemplo'...")
print(gerar_jwt("usuario_exemplo", "Matheus Makaline", True))