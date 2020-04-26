#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('\n============== COMPARAR DOIS NÚMEROS INTEIROS ==============\n')
numero1 = int(input('Insira o primeiro numero: '))
numero2 = int(input('Insira o segundo numero:'))

if numero1>numero2:
    print(f'O primeiro valor ({numero1}) é maior que o segundo ({numero2}).')
elif numero2>numero1:
    print(f'O segundo valor ({numero1}) é maior que o primeiro ({numero2}).')
else:
    print(f'Os numeros digitados são iguais ({numero1} = {numero2}).')