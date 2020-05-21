#INTERACTIVE HELP:
#help() no console do python = vai exibir o manual do qualquer função e biblioteca do python

#DOCSTRINGS:
#documentação de uma função

def contador(i, f, p):
    """
    ->Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """ #docstring
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')
# help(contador)

#PARAMETROS OPCIONAIS:
# def somar(a, b, c):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3, 2, 5)
# somar(8, 4) -> n vai funcionar pois c não esta recebendo nenhum valor

#usando o conceito de variavel opcinal
def somar(a=0, b=0, c=0): #se c não receber um valor ele vai ter o valor 0
    """
    :param a: um numero qualquer (se não informado o programa funcionara com o a valendo 0)
    :param b: um numero qualquer (se não informado o programa funcionara com o b valendo 0)
    :param c: um numero qualquer (se não informado o programa funcionara com o c valendo 0)
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')
# somar(3, 2, 5)
# somar(8, 4)

#ESCOPO DE VARIAVEIS
#local onde a variavel vai ou não existir

def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')
#função principal
n = 2
teste()
print(f'No programa principal n vale {n}')
#print(f'No programa principal x vale {x}') #vai dar erro

#RETORNO DE VARIAVEIS
#uso do comando return na função