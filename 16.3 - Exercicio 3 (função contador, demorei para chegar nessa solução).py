# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    print(inicio,' ',end='')
    while inicio != fim:
        if inicio > fim and passo<0:
            a = inicio + passo
            if (a < fim):
                break
            elif a == fim or a > fim:
                inicio += passo
                print(inicio, ' ', end='')
        elif inicio < fim and passo>0:
            a = inicio + passo
            if (a > fim):
                break
            elif a == fim or a < fim:
                inicio += passo
                print(inicio, ' ', end='')
        else:
            print('\nAlguma informação inserida esta errada')
            break

