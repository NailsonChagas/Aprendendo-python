#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

print('================================ JOKEMPÔ ================================')
print('''Suas opções:
    [0] = Pedra
    [1} = Papel
    [2] = Tesoura
''')

opção = int(input('Qual sua escolha?:'))

print('\n')
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')
sleep(1)
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Você escolheu {itens[opção]}')
print('-='*11)
print('\n')

if computador == 0:
    if opção == 1:
        print('VOCÊ VENCEU!!!!!')
    else:
        print('VOCÊ PERDEU')

if computador == 1:
    if opção == 2:
        print('VOCÊ VENCEU!!!!!')
    else:
        print('VOCÊ PERDEU')

if computador == 2:
    if opção == 0:
        print('VOCÊ VENCEU!!!!!')
    else:
        print('VOCÊ PERDEU')