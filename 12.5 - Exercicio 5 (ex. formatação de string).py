#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Geladeira', 'Fogão', 'Microondas',14.98, 7.93, 2.5)
print('=============== Lista de Preços ===============')

for i in range(0,int(len(produtos)/2)):
    print(f'{produtos[i]:-<40}R${produtos[i+3]:>5}')