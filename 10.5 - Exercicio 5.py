#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

print('========= PROGRESSÃO ARITMÉTICA =========')
primeiroTermo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))

i = 0
while i != 10:
    print(f'{primeiroTermo + (i * razão)} ', end='')
    i += 1