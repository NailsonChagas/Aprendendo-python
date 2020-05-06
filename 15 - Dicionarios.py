#estrutura de dados semelhantes a listas, porem possui indice literal
# tupla = ()
# listas = []
# dicionario = {}
# dicionario.values() ->acessa os valores do dicionario
# dicionario.keys() ->acessa as chaves do dicionario
# dicionario.items() ->acessa os itens do dicionario

dados = dict() #dizendo q a variavel dados é um dicionario ou dados = {}
dados = {'nome':'Nailson','idade':20}
print(dados)
print(dados['nome'])
print(dados['idade'])

#inserir elemento em um dicionario
dados['sexo'] = 'Masculino'
print(dados)

#deletando um elemento
del dados['idade']
print(dados)

#ex no laço
filme = {
         'titulo':'Star Wars', #valor: Star Wars / chave: titulo/ item: Star Wars + titulo
         'ano':1977, #valor: 1977 /  chave: ano / item:1977 + ano
         'diretor':'George Lucas'#valor: George lucas / chave: diretor/ item: George lucas + diretor
        }

for k,v in filme.items():
    print(f'O {k} é {v}')