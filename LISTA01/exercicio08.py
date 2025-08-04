try:
    qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))

    if qtd_alunos <= 0:
        print("Quantidade inválida. Deve ser maior que zero.")
    else:
        notas = []

        for i in range(1, qtd_alunos + 1):
            while True:
                try:
                    nota = float(input(f"Digite a nota do aluno {i}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida. Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")

        media = sum(notas) / len(notas)
        maior = max(notas)
        menor = min(notas)

        print(f"\nAnálise de Notas da Turma:")
        print(f"Quantidade de alunos: {qtd_alunos}")
        print(f"Média geral da turma: {media:.2f}")
        print(f"Maior nota: {maior:.2f}")
        print(f"Menor nota: {menor:.2f}")
        
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
