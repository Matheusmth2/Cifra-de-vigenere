def vigenere_cipher(text, key):
    encrypted_text = "" # Armazena o texto final cifrado
    key_index = 0   # Rastreia qual letra da chave deve ser usada no momento.
    key = key.upper() # Padroniza a chave para letras maiúsculas para facilitar o cálculo do deslocamento.

    for char in text:
        if char.isalpha(): #Verificar se é uma letra
            # Calcula o deslocamento com base na letra da chave
            # ord() pega o valor numérico ASCII da letra.
            # Subtrair ord('A') transforma a letra da chave em um número de 0 a 25 (onde 'A'=0, 'B'=1, etc.). Esse é o tamanho do deslocamento.
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                # Realiza a cifra de Vigenère para letras maiúsculas
                new_char = chr((ord(char) - ord('A') + shift) %26 + ord('A'))
            else:
                # Realiza a cifra de Vigenère para letras minúsculas
                new_char = chr((ord(char) - ord('a') + shift) %26 + ord('a'))
                # Converte a letra do texto para seu valor numérico (0 a 25), soma o deslocamento (shift), aplica o operador módulo (% 26) para dar a volta no alfabeto se passar de 'Z'/'z', e reconverte para caractere usando chr()
            encrypted_text += new_char
            # Atualiza o índice da chave para a próxima letra
            key_index = (key_index + 1) % len(key)
            #Adiciona a letra cifrada ao texto final.
            # key_index = (key_index + 1) % len(key) faz o índice da chave voltar para 0 quando chega ao final da palavra-chave, repetindo-a indefinidamente.
        else:
            # Mantém caracteres que não são letras ex: números, espaços, pontuação, etc. sem alteração.
            encrypted_text += char
        
    return encrypted_text

texto = "Matheus8"
chave = "Oi"
texto_cifrado = vigenere_cipher(texto, chave)
print(texto_cifrado)

""" A Cifra de Vigenère é um clássico método de criptografia de substituição polialfabética criado no século XVI. Ao contrário da Cifra de César (que usa sempre o mesmo deslocamento), a de Vigenère utiliza uma palavra-chave para mudar o deslocamento de cada letra, tornando-a muito mais segura para a sua época.

Como Funciona
A Palavra-Chave: Você escolhe uma palavra secreta (ex: SOL).
Repetição: A palavra é repetida até alinhar com o tamanho da mensagem que você quer cifrar.

A Tabela (Tabula Recta): Cada letra da mensagem é cruzada com a letra correspondente da chave em uma matriz de 26x26 alfabetos deslocados para encontrar a letra cifrada.

Exemplo Prático:
Mensagem: OLA
Chave: SOL (repetida)
OBS: Se a mensagem fosse maior que a chave, a chave se repete até cobrir toda a mensagem.
    EX: Mensage: TERRA, a Chave: SOL iria ficar assim: SOLSO, se fosse maior ainda, a chave se repetiria novamente: SOLSOSOL...

Cifragem:

Letra O + Chave S = Letra cifrada G
Letra L + Chave O = Letra cifrada Z
Letra A + Chave L = Letra cifrada L

Mensagem Cifrada: GZL

Por que ela era considerada "indestrutível"?
Durante séculos, ela foi chamada de le chiffre indéchiffrable (o código indestrutível) porque a mesma letra no texto original (por exemplo, a letra "A") podia ser representada por letras diferentes no texto cifrado, dependendo da sua posição na palavra-chave. Isso quebrava a análise de frequência simples que derrotava a Cifra de César.

Como foi quebrada?
No século XIX, o matemático Charles Babbage e o oficial Friedrich Kasiski descobriram que, se a mesma palavra-chave coincidisse com trechos repetidos da mensagem, geraria padrões repetidos no texto cifrado. Isso permitia deduzir o tamanho da chave e, depois, quebrar cada letra como se fosse uma Cifra de César isolada. """