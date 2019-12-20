#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Insira o seu salario: '))

if salario > 1250:
    aumento = salario + (salario*10/100)
    print(f'O salario de R${salario:.2f} recebeu um aumento de 10%, o que resulta em R${aumento:.2f}')
else:
    aumento = salario + (salario*15/100)
    print(f'O salario de R${salario:.2f} recebeu um aumento de 15%, o que resulta em R${aumento:.2f}')