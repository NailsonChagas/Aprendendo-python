#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
ladoA = float(input('Insira o tamanho do lado A: '))
ladoB = float(input('Insira o tamanho do lado B: '))
ladoC = float(input('Insira o tamanho do lado C: '))

if (ladoA + ladoB) > ladoC and (ladoA + ladoC) > ladoB and (ladoC + ladoB) > ladoA:
    print(f'As retas A = {ladoA}, B = {ladoB} e C = {ladoC} podem formar um triangulo!')
else:
    print(f'As retas A = {ladoA}, B = {ladoB} e C = {ladoC} não podem formar um triangulo.')