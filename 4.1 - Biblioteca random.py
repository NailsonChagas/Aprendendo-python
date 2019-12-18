#pra baixar módulos: https://pypi.org/
import emoji #biblioteca q eu baixei
import random #biblioteca que vem com a linguagem
numero = random.random() #gera um numero float entre 0 e 1
print(f'random.random() = {numero}')
numero = random.randint(1, 10) #random.randint(1, 10) vai gerar um numero int entre 1 e 10
print(f'random.randint(1, 10) = {numero}')

print(emoji.emojize('Ola mundo :earth_americas:', use_aliases=True))

