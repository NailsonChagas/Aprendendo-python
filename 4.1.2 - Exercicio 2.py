#leia os comprimentos dos catetos de um triangulo e retangulo e mostre o tamanho de sua hipotenusa
from math import sqrt, pow
catetoAdjacente = float(input('Insira o tamanho do cateto adjacente: '))
catetoOposto = float(input('Insira o tamanho do cateto oposto: '))

hipotenusa = sqrt(pow(catetoAdjacente,2) + pow(catetoOposto, 2))

print(f'O tamanho da hipotenusa é: {hipotenusa:.3f}')