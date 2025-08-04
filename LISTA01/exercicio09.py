"""palindromo"""

import unicodedata

def limpar_texto(texto):
    # Remove acentos, transforma em minúsculas e remove espaços e pontuações
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'  # remove acentos
    )
    texto = ''.join(c for c in texto if c.isalnum())  # remove espaços e pontuação
    return texto

# Entrada
entrada = input("Digite uma palavra ou frase: ")

# Limpeza do texto
texto_limpo = limpar_texto(entrada)

# Verificação de palíndromo
if texto_limpo == texto_limpo[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
