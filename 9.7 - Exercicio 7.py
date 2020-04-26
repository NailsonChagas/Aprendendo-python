#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

entrada = int(input('Insira um numero: '))
contadorDiv = 0

for i in range (2,entrada):
    if entrada % i == 0:
        contadorDiv += 1
if contadorDiv == 0:
    print(f'{entrada} é primo')
else:
    print(f'{entrada} não é primo')