import os

dicionario = {
    'Soma' : '+',
    'Subtração' : '-',
    'Divisão' : '/',
    'Multiplicação' : '*'
}

while True:
    print('Olá, tudo bem?')

    print("""=========================================================
          (1) Soma
          (2) Subtração
          (3) Divisão
          (4) Multiplicação

          Digite FIM para finalizar a calculadora. 
=====================================================================""")
    
    decisao = input('Qual operação deseja realizar?').upper
    
    if decisao == 'FIM':
        os.system('cls')
        break
    
    if decisao == '1':
        print('Ótimo, vamos realizar a Soma:')
        num1 = input('Digite seu primeiro número > ')        
        num2 = input('Digite seu segundo número > ')
        resultado = num1 + num2
        print(f'O resultado da Soma de {num1} e {num2} é de {resultado}')
    
    elif decisao == '2':
        print('Ótimo, vamos realizar a Subtração:')
        num1 = input('Digite seu primeiro número > ')        
        num2 = input('Digite seu segundo número > ')
        resultado = num1 - num2
        print(f'O resultado da Subtração de {num1} e {num2} é de {resultado}')

    elif decisao == '3':
        print('Ótimo, vamos realizar a Divisão:')
        num1 = input('Digite seu primeiro número > ')        
        num2 = input('Digite seu segundo número > ')
        resultado = num1 / num2
        print(f'O resultado da Divisão de {num1} e {num2} é de {resultado}')
    
    elif decisao == '4':
        print('Ótimo, vamos realizar a Multiplicação:')
        num1 = input('Digite seu primeiro número > ')        
        num2 = input('Digite seu segundo número > ')
        resultado = num1 * num2
        print(f'O resultado da Multiplicação de {num1} e {num2} é de {resultado}')
    else:
        print('Poxa, parece que você não escolheu nenhuma das opções apresentadas, vamos começar denovo?')
        decisao2 = input('Digite Sim/Não se gostaria de começar denovo: ').upper
        if decisao2 == 'SIM':
            os.system('cls')
        else:
            os.system('cls')
            break


