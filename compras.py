produtos = []
total = 0

for i in range(1, 4):
    nome = input(f"Digite o nome do produto {i}: ")
    
    while True:
        try:
            preco = float(input(f"Digite o preço do produto {i} (R$): "))
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    produtos.append((nome, preco))
    total += preco

# Verifica e aplica o desconto
desconto = 0
if total > 100:
    desconto = total * 0.10

valor_final = total - desconto

# Exibe resultados
print("\nResumo da Compra:")
for nome, preco in produtos:
    print(f"- {nome}: R${preco:.2f}")

print(f"\nTotal: R${total:.2f}")
if desconto > 0:
    print(f"Desconto (10%): -R${desconto:.2f}")
print(f"Valor Final: R${valor_final:.2f}")
