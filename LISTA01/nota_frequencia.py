nota = float(input("Digite a nota do aluno (0 a 10): "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if nota >= 6.0 and frequencia >= 75:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")


"""1: Porque o aluno só será aprovado se atender simultaneamente a duas condições:

Nota maior ou igual a 6.0

Frequência maior ou igual a 75%

O operador and exige que ambas as condições sejam verdadeiras para que o resultado geral seja True. Isso reflete a regra do enunciado corretamente: ambas as exigências devem ser atendidas."""

"""2. O que aconteceria se fosse usado or no lugar de and?
Se fosse usado or:

if nota >= 6.0 or frequencia >= 75:
O aluno seria aprovado mesmo se só uma das condições fosse atendida. Isso não respeita a regra fornecida, pois o aluno poderia ter nota alta, mas frequência baixa e ainda ser aprovado — o que é incorreto conforme o enunciado."""