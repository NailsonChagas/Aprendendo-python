#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

#tuplaNumeros = (int(input('Insira o 1º numero: ')), int(input('Insira o 2º numero: ')), int(input('Insira o 3º numero: ')), int(input('Insira o 4º numero: ')))
#ou ainda:
tuplaNumeros = tuple(int(input(f'Digite o valor:'))for i in range (0,4)) #repete o comando input 4x e cria um tupla

print(f'Tupla inserida: {tuplaNumeros}')
print(f'O numero 9 apareceu {tuplaNumeros.count(9)} vezes')
print(f'A primeira possição em que o 3 apareceu foi {tuplaNumeros.index(3)+1}º posição')
print('Numeros primos: ', end='')
for i in range(0,4):
    if(tuplaNumeros[i]%2 == 0):
        print(f'{tuplaNumeros[i]} ', end='')