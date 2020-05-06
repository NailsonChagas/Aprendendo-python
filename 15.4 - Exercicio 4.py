# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dicionarioCadastro = dict()
gols = list()
soma = 0
dicionarioCadastro['Nome'] = str(input('Nome do Jogador: '))
numeroDePartidas = int(input(f'Quantas partidas {dicionarioCadastro["Nome"]} jogou?: '))
for i in range(0,numeroDePartidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}?: ')))
    soma += gols[i]
dicionarioCadastro['Gols'] = gols
dicionarioCadastro['Total'] = soma
print('-='*15)
print(dicionarioCadastro)
print('-='*15)
for k,v in dicionarioCadastro.items():
    print(f'O campo {k} tem valor: {v}')
print('-='*15)
print(f'O jogador {dicionarioCadastro["Nome"]} jogou {numeroDePartidas} partidas')
for i in range(0,numeroDePartidas):
    print(f'   => Na partida {i+1}, fez {gols[i]} gols')