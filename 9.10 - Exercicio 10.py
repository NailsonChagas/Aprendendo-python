#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

for i in range (0,5):
    peso = int(input(f'Insira o peso da {i+1}ª:'))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso

print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg')