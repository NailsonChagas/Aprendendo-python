# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(*numeros):
    i = 0
    for valor in numeros:
        if valor > i:
            i = valor
    print(i)

maior(9,8,6,7,2,3,4,1,10)