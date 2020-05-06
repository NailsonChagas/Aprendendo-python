# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)}
print('RESULTADOS: ')

for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(0.65)

ranking = dict()
ranking = sorted(jogadores.items(), key=itemgetter(1)) #itemgetter(0) usaria a parte Jogador
print('-='*13)
print('RANKING: ')
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.2)