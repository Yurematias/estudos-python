op = 0

while (op != 4):
    print('-----------------------')
    print('-----    MENU    ------')
    print('-----------------------')
    print('1 - Calcular média')
    print('2 - Potenciação')
    print('3 - Numeros primos')
    print('4 - Sair')

    op = int(input('Digite a opção desejada: '))

    if op == 1:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))
        print(f'A media entre {num1} e {num2} é {(num1+num2)/2}')
    elif op == 2:
        num1 = float(input('Digite o primeiro numero: '))
        num2 = float(input('Digite o segundo numero: '))
        print(f'{num1} elevado a {num2} é {num1**num2}')
    elif op == 3:
        numInt = int(input('Digite um numero: '))

        numeroPrimo = True
        for i in range(2, numInt):
            if numInt % i == 0:
                numeroPrimo = False
        
        print(f'O número {numInt} é primo' if numeroPrimo else f'O número {numInt} não é primo')        
    elif op == 4:
        print('Fim de execução')
    else:
        print('opção inválida')
