# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(0,5):
    num = int(input(f'Insira o {i+1}º numero: '))

    if i == 0 or num > lista[len(lista)-1]:
        lista.append(num)
        print(lista)
        print('-=-'*11)
    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição,num)
                print(f'Adicionado na posição {posição} da lista')
                print(lista)
                print('-=-' * 11)
                break
            posição += 1
