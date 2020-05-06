# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
lista = list()

while True:
    dicionarioCadastro = dict()
    gols = list()
    soma = 0
    dicionarioCadastro['Nome'] = str(input('Nome do Jogador: '))
    dicionarioCadastro['Numero De Partidas'] = int(input(f'Quantas partidas {dicionarioCadastro["Nome"]} jogou?: '))
    for i in range(0, dicionarioCadastro['Numero De Partidas']):
        gols.append(int(input(f'Quantos gols na partida {i + 1}?: ')))
        soma += gols[i]
    dicionarioCadastro['Gols'] = gols
    dicionarioCadastro['Total'] = soma
    lista.append(dicionarioCadastro)
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()
    if escolha != 'S':
        del dicionarioCadastro
        print('-=' * 18)
        break
    else:
        print('-=' * 18)
for i in range(0,len(lista)):
    print(f'Jogador {i+1}:')
    for k,v in lista[i].items():
        print(f'  O campo {k} tem valor: {v}')
    print(f'O jogador {lista[i]["Nome"]} jogou {lista[i]["Numero De Partidas"]} partidas')
    for i in range(0, lista[i]['Numero De Partidas']):
        print(f'  => Na partida {i + 1}, fez {gols[i]} gols')
    print('-=' * 18)


