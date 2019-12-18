#leia 4 nomes e os mor=stre em ordem aleatória
from random import shuffle
nome1 = str(input('Insira o nome 1: '))
nome2 = str(input('Insira o nome 2: '))
nome3 = str(input('Insira o nome 3: '))
nome4 = str(input('Insira o nome 4: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista) #shuffle vai embaralhar os elementos dessa lista

print(f'{lista}')