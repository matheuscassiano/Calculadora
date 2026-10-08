# Calculadora com Python3
import os
while True:

    # Perguntar qual é o tipo de operação
    operacao = input('Qual opreração (+, -, *, /, P, R)? ou \'Q\' para sair ')
    if operacao == 'Q' or operacao == 'q':
        break

    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' or operacao == 'P' or operacao == 'p' or operacao == 'R' or operacao == 'r':    
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
            
        elif operacao == 'P' or operacao == 'p':
            result = x ** y
            
        elif operacao == 'R' or operacao == 'r':
            result = x ** 1/y
            
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
