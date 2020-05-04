# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
numeroLinhas = int(input('Quantos jogos serão feitos?: '))
matriz = []

for i in range(0,numeroLinhas):
    lista = []
    for j in range(0, 6):
        lista.append(randint(1, 60))
    matriz.append(lista)

print('-_'*15)
print('Palpites: ')
for i in range(0,numeroLinhas):
    print(f'Jogo {i+1}: ', end='')
    for j in range (0, 6):
        if j!=5:
            print(f'{matriz[i][j]}\t', end='')
        else:
            print(f'{matriz[i][j]}')