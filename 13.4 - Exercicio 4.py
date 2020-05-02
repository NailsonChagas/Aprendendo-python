# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
i = 0
while True:
    lista.append(int(input(f'Insira o {i+1}º numero: ')))
    i += 1
    escolha = str(input('Deseja constinuar?[S/N]: '))
    if escolha in 'Nn':
        break
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O numero 5 aparece na lista na posição {lista.index(5)}')
else:
    print('O numero 5 não aparece na lista')