#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = []
for i in range(0,3):
    lista = []
    for j in range(0, 3):
        lista.append(int(input(f'Linha: {i} Coluna: {j} -> Insira um numero inteiro: ')))
    matriz.append(lista)
print('-_'*24)

somaPares = 0
somaTerceiraColuna = 0
print('Matriz inserida: ')
for i in range(0,3):
    for j in range (0, 3):
        if j!=2:
            print(f'{matriz[i][j]}\t', end='')
        else: #j==2 ->terceira coluna
            print(f'{matriz[i][j]}')
            somaTerceiraColuna += matriz[i][j]

        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]

print(f'A soma de todos os números pares: {somaPares}')
print(f'A soma dos valores da terceira coluna: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')