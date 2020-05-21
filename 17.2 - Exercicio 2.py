# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.

def fatorial(entrada, mostrar=False):
    fat = 1
    for i in range(1, entrada+1):
        fat *= i
    if mostrar == True:
        for i in range(1, entrada+1):
            if i == 1:
                print(f'{entrada}! = ',end='')
            if i == (entrada):
                print(f'{i} = {fat}', end='')
            else:
                print(f'{i} * ', end='')
    else:
        print(fat)
fatorial(int(input('Insira um numero: ')), bool(int(input('Deseja mostrar o calculo do fatoria(1/0): '))))