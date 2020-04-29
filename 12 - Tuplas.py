#tupla é uma variarel composta, parece com um vetor que não pode ser alterado com a execução do programa
#len() -> função mostra qual o tamanho da tupla
#sorted() -> coloca em ordem, porem como uma tupla é imutavel essa função não pode ser aplicada diretamente a tupla
#ex:

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))
#lanche[1] = 'Refrigerante' -> n executa -> tupla é imutavel
print(lanche[1:3]) #vai do elemento 1 ao 3(ignora o 3, então mostra 1 e 2)
print(lanche[-2])
print(lanche[-2:])
print(lanche[:-2])
print(f'{lanche[1]}\n')

print('=-='*11)
for i in range (0, len(lanche)):
    print(lanche[i])
    print(i)

print('=-='*11)
for i in lanche:
    print(i)

print('=-='*11)
for posição, i in enumerate(lanche):
    print(f'Posição: {posição}   Comida: {i}')

print('=-='*11)
lista = sorted(lanche) #ou ainda: print(sorted(tupla))
print(lanche)
print(lista)