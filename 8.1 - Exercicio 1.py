#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

salario = float(input('Insira o seu salário: '))
valor = float(input('Insirea o valor do imóvel desejado: '))
tempo = int(input('Em quantos anos você gostaria de quitar o imóvel: '))

print('\n============== EMPRÉSTIMO BANCÁRIO ==============\n')

prestação = valor / (tempo*12)
print(f'O valor da prestação mensal é R${prestação:.2f}')
if prestação > (salario*30/100):
    print('O seu empréstimo infelizmente não podera ser aprovado.')
else:
    print('Empréstimo podera ser efetuado.')