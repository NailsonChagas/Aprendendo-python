#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('========= PROGRESSÃO ARITMÉTICA =========')
primeiroTermo = int(input('Digite o primeiro termo da P.A: '))
razão = int(input('Digite a razão da P.A: '))
quantosTermos = int(input('Quantos termos deseja mostrar: '))

i = 0
while i != quantosTermos:
    print(f'{primeiroTermo + (i * razão)} ', end='')
    i += 1