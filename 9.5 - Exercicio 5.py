#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for i in range (0,6):
    entrada = int(input(f'Digite o {i+1}º numero: '))
    if entrada % 2 == 0:
        soma = soma + entrada
print(f'A soma dos numeros pares é {soma}')