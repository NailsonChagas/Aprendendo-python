#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

print('============================= TABUADA =============================')
numero = int(input('Digite um numero: '))

for i in range (0,11):
    print(f'{numero} * {i} = {numero*i}')