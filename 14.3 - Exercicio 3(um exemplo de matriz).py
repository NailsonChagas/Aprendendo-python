# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
print('================= Criar Matriz =================')
matriz = []
for i in range(0,3):
    lista = []
    for j in range(0, 3):
        lista.append(int(input(f'Linha: {i} Coluna: {j} -> Insira um numero inteiro: ')))
    matriz.append(lista)
print('-_'*24)
print('Matriz inserida: ')
for i in range(0,3):
    for j in range (0, 3):
        if j!=2:
            print(f'{matriz[i][j]}\t', end='')
        else:
            print(f'{matriz[i][j]}')