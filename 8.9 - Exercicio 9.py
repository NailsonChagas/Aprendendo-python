#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('============================= LOJAS GUANABARA =============================')

preço = float(input('Preço das compras: R$'))

print('''Opção de pagamento:
[1] = a vista dinheiro/cheque
[2] = a vista no cartão
[3] = 2x no cartão
[4] = 3x ou mais no cartão
''')

opção = int(input('Qual a opção?: '))

if opção == 1:
    print(f'O pagamento sera feito a vista por R${preço - (preço/10)}')
elif opção == 2:
    print(f'O pagamento será feito a vista por R${preço - (preço*5/100)}')
elif opção == 3:
    print(f'O pagamento será feito em duas parcelas de R${preço/2}')
elif opção == 4:
    parcelas = int(input('Em quantas parcelas sera feito o pagamento?: '))
    if parcelas >= 3:
        print(f'O pagamento será feito em {parcelas} parcelas de {preço + (preço*20/100)}')
    else:
        print('Opção invalida')
else:
    print(f'Opção inválida')