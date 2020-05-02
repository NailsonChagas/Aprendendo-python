# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
listaPar = []
listaImpar = []
i = 0
while True:
    lista.append(int(input(f'Insira o {i+1}º numero: ')))
    i += 1
    escolha = str(input('Deseja constinuar?[S/N]: '))
    if escolha in 'Nn':
        print('-_'*13)
        break
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])
print(f'Lista original: {lista}')
print(f'Numeros pares: {listaPar}')
print(f'Numeros impares: {listaImpar}')