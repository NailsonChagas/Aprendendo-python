#Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range (1,51): #de 1 a 50 verificando se i % 2 == 0
    print('.', end='')
    if i % 2 == 0:
        print(f'{i} ', end='')

#ou
print('\n')

for i in range (2,51,2): #de 2 a 51 pulando de 2 em 2
    print('.', end='')
    print(f'{i} ', end='')