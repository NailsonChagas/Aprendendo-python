#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for i in range(0,5):
    lista.append(int(input(f'Insira o {i + 1}º numero inteiro: ')))
print(f'Os numeros digitados foram: {lista}')
print(f'O maior valor da lista é o {max(lista)} e está na posição {lista.index(max(lista))} da lista')
print(f'O menor valor da lista é o {min(lista)} e está na posição {lista.index(min(lista))} da lista')