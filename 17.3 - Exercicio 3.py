# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = '', gols = ''):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    if nome == '':
        jogador = '<desconhecido>'
    else:
        jogador = nome
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')

ficha(str(input('Nome do jogador: ')), input('Número de gols marcados: '))