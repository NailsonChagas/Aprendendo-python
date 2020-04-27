#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

i = 0
soma = 0
contador = 0
while i!= 999:
    i = int(input(f'Insira o {contador+1}º número: '))
    if i!=999:
        contador += 1
        soma += i
    else:
        print(f'Foram digitados {contador} números')
        print(f'A soma entre eles resultou em {soma}')