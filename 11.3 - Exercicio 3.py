#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

i = 0

print('======== ÍMPAR OU PAR ========')

while True:
    jogador = -1
    escolha = 'b'
    while (jogador<0) or (jogador>5):
        jogador = int(input('Insira um número de 0 a 5: '))
        if (jogador >= 0) and (jogador <= 5):
                escolha = str(input('Impar ou par?[I/P]: ')).upper()
        else:
            print('Insira um número válido')
    npc = randint(0, 5)
    resultado = npc + jogador

    if escolha == 'I':
        if resultado%2 != 0:
            i += 1
            print(f'PC: {npc}  JOGADOR: {jogador}')
            print('Você venceu a rodada!!!')
            print('=-'*15)
        else:
            print(f'PC: {npc}  JOGADOR: {jogador}')
            print('Você perdeu a rodada :(')
            print('=-' * 15)
            break
    elif escolha == 'P':
        if resultado%2 == 0:
            i += 1
            print(f'PC: {npc}  JOGADOR: {jogador}')
            print('Você venceu a rodada!!!')
            print('=-' * 15)
        else:
            print(f'PC: {npc}  JOGADOR: {jogador}')
            print('Você perdeu a rodada :(')
            print('=-' * 15)
            break
    else:
        print('Insira uma escolha válida')

print(f'Total de vitórias consecutivas: {i}')