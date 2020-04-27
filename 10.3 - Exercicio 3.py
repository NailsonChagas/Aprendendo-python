#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

i = 0
while i != 5:
    numero1 = float(input('Primeiro valor: '))
    numero2 = float(input('Segundo valor: '))
    print("""
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Sair do programa 
    """)
    i = int(input('Opção escolhida: '))
    if i == 1:
        print(f'A soma entre {numero1} + {numero2} = {numero1 + numero2}')
    elif i == 2:
        print(f'O produto entre {numero1} * {numero2} = {numero1 * numero2}')
    elif i == 3:
        if numero1 > numero2:
            print(f'O maior numero entre os dois é {numero1}')
        elif numero1 == numero2:
            print(f'Os numeros são iguais')
        else:
            print(f'O maior numero entre os dois é {numero2}')
    elif i == 4:
        print('INSIRA SEUS NOVOS NUMEROS')
    elif i == 5:
        print('O progama esta sendo fechado')
    else:
        print('Opção invalida')

    print('=-' * 11)