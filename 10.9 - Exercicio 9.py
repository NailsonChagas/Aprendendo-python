#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

i = ''
numero = 0
soma = 0
contador = 0
maior = 1
menor = 1

print('========= MÉDIA =========')

while i != 'N':
    numero = int(input(f'Insira o {contador+1}º número: '))
    soma += numero
    contador += 1
    if numero>=maior:
        maior = numero
    if numero<=menor:
        menor = numero
    i = str(input('Deseja continuar a inserir números?[S/N]: ')).strip().upper()
    if i != 'S':
        print(f'\nA média entre os valores digitados é {soma/contador:.2}')
        print(f'O maior número digitado foi {maior} e o menor {menor}')