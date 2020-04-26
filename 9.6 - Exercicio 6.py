#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('================= Progressão Aritmética =================')

primeiroTermo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))

for i in range (0,10):
    print(f'{primeiroTermo + razão} ', end='')
    primeiroTermo = primeiroTermo + razão