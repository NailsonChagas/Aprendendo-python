#ordem de precedencia dos operadores: (), **, (*, /, //, %), (+, -)

numero1 = int(input('Insira um numero:'))
numero2 = int(input('Insira outro numero:'))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 #vai resultar em um numero float
divisaoInteira = numero1 // numero2 #vai pegar apenas a parte inteira da divisão
resto = numero1 % numero2
potencia = numero1 ** numero2 #potencia por operador aritmético

potencia2 = pow(numero1, numero2) #potencia por função

print(f'\nA soma entre {numero1} + {numero2} é: {soma}')
print(f'A subtração entre {numero1} - {numero2} é: {subtracao}')
print(f'O produto entre {numero1} * {numero2} é: {multiplicacao}')
print(f'{numero1} dividido por {numero2} é: {divisao}')
print(f'A divisão inteira {numero1} e {numero2} é: {divisaoInteira}')
print(f'O resto entre {numero1} e {numero2} é: {resto}')
print(f'{numero1} elevado a {numero2} é: {potencia}')
print(f'Outra forma de fazer a potencia: pow({numero1}, {numero2}) é {potencia2}')

#uso dos operadores em strings
print('\nOla'+'Meu Consagrado')
print('Bom dia ' * 5)

#formatação no print
nome = input('\nQual é o seu nome?: ')
print(f'Ola {nome}! ', end='') #end = '' : faz com q a linha n se quebre
print(f'Ola {nome:>30}!') #reserva 30 espaços para string e posiciona a string no final
print(f'Ola {nome:<30}!') #reserva 30 espaços para string e posiciona a string no inicio

num = 1/3
print(f'1 dividido por 3 com 4 casas após a virgula: {num:.4f}') #:.4f - quatro algarismos após o ponto flutuante