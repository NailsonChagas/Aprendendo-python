# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
matriz = []
listaNotas = []
while True:
    lista = []
    notas = []
    lista.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    lista.append((notas[0]+notas[1])/2)
    listaNotas.append(notas)
    matriz.append(lista)
    escolha = str(input('Deseja continuar?: '))
    if escolha not in 'Ss':
        del lista
        del notas
        break
print('-_'*11)
print('No.\tNOME\t\tMÉDIA')
for i in range(0, len(matriz)):
    print(f'{i}\t',end='')
    for j in range(0,2):
        if j!=1:
            print(f'{matriz[i][j]}\t\t\t', end='')
        else:
            print(f'{matriz[i][j]:.2f}')
print('-_'*11)
while True:
    aluno = int(input('Deseja ver as notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    else:
        print(f'Notas do(a) aluno(a): {matriz[aluno][0]}: {listaNotas[aluno]}')