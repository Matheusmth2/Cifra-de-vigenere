def vigenere_cipher(text, key):
    encrypted_text = ""
    key_index = 0
    key = key.upper() #Para garantir que a chave seja sempre maiúscula

    for char in text:
        if char.isalpha(): #Verificar se é uma letra
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) %26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) %26 + ord('a'))
            encrypted_text += new_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
        
    return encrypted_text

texto = "Matheus"
chave = "Oi"
texto_cifrado = vigenere_cipher(texto, chave)
print(texto_cifrado)