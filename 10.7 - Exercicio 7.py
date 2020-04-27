#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('====== SEQUÊNCIA DE FIBONACCI ======')
numero = int(input('Insira um número: '))

i = 0
fibonacci = 0
numeroAnterior = 1

while i!= numero:
    if i != numero-1:
        print(f'{fibonacci} - ', end='')
    else:
        print(f'{fibonacci}')
    fibonacci += numeroAnterior
    numeroAnterior = fibonacci - numeroAnterior
    i += 1