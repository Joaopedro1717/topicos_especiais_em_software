"""Caixa eletronico"""
try:
    saque = float(input('Digite o valor do saque: '))
    if saque <= 0:
        print('Valor inválido. O saque deve ser maior que zero.')
    elif saque % 10 != 0:
        print('Valor inválido. O saque deve ser múltiplo de 10.')
    else:
        cedulas_100 = int(saque // 100)
        saque = saque % 100

        cedulas_50 = int(saque // 50)
        saque = saque % 50

        cedulas_20 = int(saque // 20)
        saque = saque % 20

        cedulas_10 = int(saque // 10)
        saque = saque % 10

        print("\nCédulas para o saque:")
        if cedulas_100 > 0:
            print(f'{cedulas_100} cédula(s) de R$ 100,00')
        if cedulas_50 > 0:
            print(f'{cedulas_50} cédula(s) de R$ 50,00')    
        if cedulas_20 > 0:
            print(f'{cedulas_20} cédula(s) de R$ 20,00')
        if cedulas_10 > 0:
            print(f'{cedulas_10} cédula(s) de R$ 10,00')
            
except ValueError:
    print('Entrada inválida. Por favor, digite um valor válido.')