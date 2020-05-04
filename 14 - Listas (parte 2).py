dados = list() #diz q dados é uma variavel complexa do tipo dados
dados.append('pedro')
dados.append('1')
print(dados)

#uma lista de listas -> matriz
pessoas = list()
pessoas.append(dados)
print(pessoas)
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[0]) #vai mostra o item 0 da lista pessoas (q vai ser a lista dados)