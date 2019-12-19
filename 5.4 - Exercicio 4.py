#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual seu nome: '))
n = 'Silva' in nome
print(f'Seu nome possui Silva: {n}')