numero = int(input("Digite um número para ver sua tabuada: "))
intervalo = int(input("Digite o intervalo para a tabuada: "))

print(f"\nTabuada do {numero} até {intervalo}:")
for i in range(1, intervalo + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
