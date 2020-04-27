#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print('=========== FATORIAL ===========')
numero = int(input('Digite um numero: '))

multiplica = 1
print(f'{numero}! = ', end='')
while numero != 0:
    multiplica *= numero
    if numero != 1:
        print(f'{numero} x ', end='')
    else:
        print(f'{numero} = {multiplica}')
    numero -= 1
