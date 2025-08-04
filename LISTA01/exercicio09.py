"""palindromo"""

entrada = input("Digite uma palavra ou frase: ")

# Verificação de palíndromo, utiliza o [::-1] que inverte a string, faz uma comparação com o texto original, caso for igual, é um palíndromo
if entrada == entrada[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
