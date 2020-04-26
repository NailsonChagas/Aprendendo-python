#Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

i = 1
c = 10
for i in range (0,10):
    print(f'{c - i}')
    sleep(1)
    i += 1