valor1 = float(input("Digite o primeiro valor decimal: "))
valor2 = float(input("Digite o segundo valor decimal: "))

media = (valor1 + valor2) / 2

print("A média entre os dois valores é:", media)


"""1: A função input() sempre retorna os dados como string (texto), mesmo que o usuário digite um número. Para realizar cálculos numéricos, como soma ou média, o valor precisa ser convertido para um tipo numérico.

Como estamos lidando com números decimais, usamos float() para converter a string em um número de ponto flutuante.
"""

"""2:Se não usarmos float(), e apenas fizermos:

python
Copiar
Editar
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
print(valor1 + valor2)
O Python irá concatenar as strings, ou seja, vai juntar os textos."""