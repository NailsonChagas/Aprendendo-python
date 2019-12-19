frase = 'Nailson francisco chagas' #24 caracteres/ 24 espaços na memoria

print(""" Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. 
Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, 
que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. 
Seu tamanho é variável. \n""")


#tecnica de fatiamento (pegar pedaços da string)
print(frase[6])#vai pegar o ultimo n de Nailson
print(frase[0:19])#vai pegar as letras do item 0 ate o 18 (19 é excluido)
print(frase[0:24])#um numero a mais do que a quantidade contida na lista vai imprimir toda a string (0 a 23)+1
print(frase[0:24:2])#pega toda frase porem só exibira a cada duas letras
print(frase[:5]) #igual a frase[0:5]
print(frase[2:]) #vai ir do segundo item da lista até o final dela
print(frase[9::3])#igual a frase[9:(até o final):3]

#analizar uma string
print(f'\nTamanho da frase: {len(frase)}') #mostra o tamanho da string
n = frase.count('a') #diz quantas letras "a" frase tem
print(f'Quantas letras "a" a frase possui: {n}')
n = frase.count('a',0,12) #quantas letras a a lista tem da posição 0 a posição 12
print(f'Quantas letras "a" a frase tem da posição 0 a 12: {n}')
n = frase.find('an') #vai dizer onde começa an na string/ com find() se vc procura uma palavra q n existe na string ira retornar -1
print(f'Quando começa "an" na frase: {n}')
n = 'Nailson' in frase #operador que vai verificar se a palavra esta ou não na string
print(f'Existe a palavra Nailson na frase: {n} ')

#transformação
print('\n')
print(frase.replace('Nailson', 'Enilton'))#troca uma palavra por outra
print(frase.upper())#converte todas as letras minusculas para maiusculas
print(frase.lower())#converte todas as letras maiusculas para minusculas
print(frase.capitalize())#pega toda string e põe a primeira letra me maiusculo
print(frase.title())#analisa a string e onde possuir espaço a proxima letra vai ser maiuscula (a primeira letra da string fica maiuscula tbm)
frase = '   Aprenda Python  '
print(frase.strip())#tira os espaços do inicio e do final
print(frase.rstrip())#tira os espaços do final(direita)
print(frase.lstrip())#tira os espaços do inicio(esquerda)

#divisão
frase = 'Nailson Francisco Chagas'
dividido = frase.split() #dividi a frase em listas (cada palavra é uma lista)
print(f'\n{dividido[0]}')
print(f'{dividido[1]}')
print(f'{dividido[2]}')

#junção
junto = '-'.join(dividido) #vai juntar as listas usando como seperador entre elas -
print(f'\n{junto}')

