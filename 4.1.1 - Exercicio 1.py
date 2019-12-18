#crie um programa que leia um numero real qualquer e mostre na tela sua porção inteira

from math import trunc
numero = float(input('Insira um numero qualquer: '))
print(f'A parte inteira do numero digitado é {trunc(numero)}')#quando se usa o from não colocar biblioteca. na frente

