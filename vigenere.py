def vigenere_cipher(text, key):
    encrypted_text = ""
    key_index = 0
    key = key.upper() #Para garantir que a chave seja sempre maiúscula

    for char in text:
        if char.isalpha(): #Verificar se é uma letra
            # Calcula o deslocamento com base na letra da chave
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                # Realiza a cifra de Vigenère para letras maiúsculas
                new_char = chr((ord(char) - ord('A') + shift) %26 + ord('A'))
            else:
                # Realiza a cifra de Vigenère para letras minúsculas
                new_char = chr((ord(char) - ord('a') + shift) %26 + ord('a'))

            encrypted_text += new_char
            # Atualiza o índice da chave para a próxima letra
            key_index = (key_index + 1) % len(key)
        else:
            # Mantém caracteres que não são letras
            encrypted_text += char
        
    return encrypted_text

texto = "Matheus8"
chave = "Oi"
texto_cifrado = vigenere_cipher(texto, chave)
print(texto_cifrado)