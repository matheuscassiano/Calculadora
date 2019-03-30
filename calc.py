# Calculadora com Python3
import os
while True:

    # Perguntar qual é o tipo de operação
    operacao = input('Qual opreração (+, -, *, /)? ou \'Q\' para sair ')
    if operacao == 'Q' or operacao == 'q':
        break

    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':    
        # Perguntar o primeiro numero
        x = int(input('Digite o primeiro numero: '))

        # Perguntar o segundo numero
        y = int(input('Digite o segundo numero: '))

        # Calculo desses 2 numeros
        if operacao == '+':
            result = x + y

        elif operacao == '-':
            result = x - y

        elif operacao == '*':
            result = x * y

        elif operacao == '/':
            result = x / y

        else:
            print('Operação Invalida')

        # Imprimir o resultado na tela
        print(result)
        
        input('PRESS ENTER')
        os.system('clear')
        
    else:
        print('Operação Invalida')
        input('PRESS ENTER')
        os.system('clear')