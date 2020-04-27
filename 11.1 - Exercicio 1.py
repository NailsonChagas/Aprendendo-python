#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

i = 0
soma = 0

print('======= TESTE "BREAK" =======')

while True:
    numero = int(input(f'Insira o {i+1}º número: '))
    if numero != 999:
        soma += numero
        i += 1
    else:
        print(f'Foram digitados {i} números e a soma entre eles resultou em {soma}')
        break