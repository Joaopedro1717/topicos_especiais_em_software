"""Operações matemáticas com dois números"""
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

print(f'A soma dos números é: {numero1 + numero2}')
print(f'A subtração dos números é: {numero1 - numero2}')
print(f'A multiplicação dos números é: {numero1 * numero2}')

divisao = numero1 / numero2 if numero2 != 0 else 'Indefinido (divisão por zero)'

print(f'A divisão dos números é: {divisao}')