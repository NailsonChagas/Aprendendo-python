#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

print('\n================ ANALISADOR DE TRIANGULOS ================')
ladoA = float(input('Insira o lado A do triangulo: '))
ladoB = float(input('Insira o lado B do triangulo: '))
ladoC = float(input('Insira o lado C do triangulo: '))
print('==========================================================\n')

if ladoA==ladoB and ladoB==ladoC:
    print('O triangulo é EQUILÁTERO.')
elif ladoB==ladoC or ladoC==ladoA or ladoA==ladoB:
    print('O triangulo é ISÓSCELES.')
elif ladoB!=ladoC and ladoA!=ladoB and ladoC!=ladoA:
    print('O triangulo é ESCALENO')
else:
    print('O triangulo inserido é invalido.')