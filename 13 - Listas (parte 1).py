#declaração de uma lista
lista = [1,2,3,4,5,6]
listaS = ['a', 'b', 'c']

#algumas formas de ler uma lista
for i in range(0, len(lista)):
    print(lista[i])
    print(i)
print('---'*11)
for i in range(0, len(listaS)):
    print(listaS[i])
    print(i)
print('---'*11)
for i in lista:
    print(lista)
    print(i)
print('---'*11)
for i in listaS:
    print(listaS)
    print(i)

print('=-='*11)

#inserir elemento no lugar de outro elemento já existente
listaX = [4,4,4,4,4,4,4]
print(listaX)
listaX[2] = 3
print(listaX)

#inserir um NOVO elemento no FINAL da lista (Obs: A listaX originalmente possui 7 espaços, o comando usado colocara um novo elemento em uma oitava posição)
listaX.append(8)
print(listaX)
print('---'*11)

#inserir um NOVO elemento entre os outros elementos da lista (Obs: tambem vai criar um novo espaço na lista)
print('listaX.insert(0,3): Obs: colocar na posiçao 0 da lista o valor 3, os elementos seguintes a posição 0 irão deslocar uma casa')
listaX.insert(0,3)
print(listaX)
print('listaX.insert(3, ''nailson''): Obs: colocar na posiçao 3 da lista a palavra nailson, os elementos seguintes a posição 3 irão deslocar uma casa')
listaX.insert(3,'nailson')
print(listaX)
print('=-='*11)

#funções para deletar elementos de uma lista
print(listaX)
del listaX[2] #exclui o item 2 da lista e reagrupa a lista para não ficar um "buraco"
print(listaX)
listaX.pop(0) #exclui o item 0 da lista e reagrupa a lista para não ficar um "buraco"
print(listaX)
listaX.remove(4) #vai procurar o primeiro item de valor 4 e ira apaga-lo, após isso ira reagrupar a lista para não ficar um buraco
print(listaX)
listaX.pop() #se n colocarmos o indice do item a ser apagado, o ultimo item sera deletado
print(listaX)
print('=-='*11)

#uma observação muito interessante
listaY = list(range(8,20))
print(listaY)
listaZ = list(range(8,20,2)) #vai de 8 a 19(como é pulando de 2 em 2 no caso sera 18) pulando de 2 em 2
print(listaZ)
print('=-='*11)

#organizando uma lista
listaD = [9,2,7,6,1,2,3,8,2,8,4]
print(listaD)
listaD.sort() #deixa a lista em ordem crescente
print(listaD)
listaD.sort(reverse=True) #deixa a lista em ordem decrescente
print(listaD)
print(len(listaD)) #vai dizer a QUANTIDADE de elementos que a lista possui