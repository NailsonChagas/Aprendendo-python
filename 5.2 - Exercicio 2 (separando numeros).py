#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Insira um numero inteiro de 0 a 9999: '))
unidade = (num//1) % 10
dezena = (num//10) % 10
centena = (num//100) % 10
milhar = (num//1000) % 10

print(f'Analisando o numero {num}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
