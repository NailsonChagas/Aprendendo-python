#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

cont1000 = 0
nomeBarato = ''
soma = 0
cont = 0

while True:
    nomeProduto = str(input('Insira o nome do produto: '))
    preçoProduto = float(input('Insira o preço do produto: R$'))

    if cont == 0:
        barato = preçoProduto
        cont += 1

    soma += preçoProduto

    if barato >= preçoProduto :
        nomeBarato = nomeProduto

    if preçoProduto > 1000:
        cont1000 += 1

    escolha = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if escolha != 'S':
        print(f'Total gasto na compra: R${soma:.2f}')
        print(f'{cont1000} produtos custaram mais de R$1000.00')
        print(f'{nomeBarato} foi o produto mais barato')
        break
    else:
        print('=-='*12)