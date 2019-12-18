#leia o nome de quatro pessoas e mostre o nome de uma delas de forma aleatória
from random import choice
nome1 = str(input('Insira o nome do aluno 1: '))
nome2 = str(input('Insira o nome do aluno 2: '))
nome3 = str(input('Insira o nome do aluno 3: '))
nome4 = str(input('Insira o nome do aluno 4: '))

lista = [nome1, nome2, nome3, nome4]  #[] tudo dentro disso forma uma lista

print(f'O escolhido foi {choice(lista)}') #choice ira sortear um elemento da lista
