# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


listaArmazenamento = []
i = 0
peso = []
while True:
    listaCadastro = []
    listaCadastro.append(str(input(f'Insira o nome da {i+1}º pessoa: ')))
    listaCadastro.append(float(input(f'Qual o peso do(a) {listaCadastro[0]}?: ')))
    peso.append(listaCadastro[1])
    listaArmazenamento.append(listaCadastro)
    i += 1

    escolha = str(input('Deseja continuar?[S/N]: '))
    if escolha not in 'Ss':
        print('_-'*17)
        break
    else:
        continue
print(f'Foram cadastradas {len(listaArmazenamento)} pessoas')

aux = min(peso)
print(f'O menor peso foi de {aux}Kg e as pessoas com essa massa são: ', end='')
for i in range(0,len(peso)):
    if peso[i] == aux:
        print(f' {listaArmazenamento[i][0]} ', end='')

aux = max(peso)
print(f'\nO maior peso foi de {aux}Kg e as pessoas com essa massa são: ', end='')
for i in range(0,len(peso)):
    if peso[i] == aux:
        print(f' {listaArmazenamento[i][0]} ', end='')