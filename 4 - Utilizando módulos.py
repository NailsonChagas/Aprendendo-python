#os imports ficaram nas primeiras linha do programa
#para ver os modulos q vem com o python: https://docs.python.org/3/
#módulos == bibliotecas
#módulo math: ceil(arredonda pra cima), floor(arredonda pra baixo), trunc(elimina os numeros depois da virgula), pow(potencia), sqrt(raiz quadrada), factorial(fatorial)
# import math: importa todas as funções do módulo math
# from math import sqrt, ceil: importa apenas a função sqrt e ceil do módulo math

import math
numero = int(input('Insira um numero inteiro: '))
raiz = math.sqrt(numero)
print(f'A raiz de {numero} é {raiz:.3f}, arredondando pra cima é {math.ceil(raiz)} e arredondando pra baixo é {math.floor(raiz)}')

