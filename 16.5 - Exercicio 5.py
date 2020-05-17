# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
from random import sample, randint

def sorteiaSemRepeticao():
    lista = sample(range(0,11),5)
    print(lista)

def sorteia():
    lista = list()
    for i in range(0,5):
        lista.append(randint(0,10))
    return lista

def somaPar():
    lista = sorteia()
    print(lista)
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    return soma

print(somaPar())