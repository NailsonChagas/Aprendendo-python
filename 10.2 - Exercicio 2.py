#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('======= Jogo da Advinhação =======')

numeroSorteado = randint(0,10)

i = -1
contador = 0

while i!=numeroSorteado:
    i = int(input('Insira um número de 0 a 10: '))
    contador += 1
    if i == numeroSorteado:
        print('Parabens você ganhou!!!!')
    else:
        print('Tente outra vez ;(')

print(f'O numero de tentativas necessarias para ganhar foi: {contador}')