#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
massa = float(input('Insira a massa em Kg da pessoa: '))
altura = float(input('Insira a altura da pessoa em metros: '))
imc = massa / (altura**2)

if imc < 18.5:
    print(f'IMC: {imc:.1f}, com esse IMC a pessoa esta abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'IMC: {imc:.1f}, com esse IMC a pessoa esta no peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'IMC: {imc:.1f}, com esse IMC a pessoa esta com sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'IMC: {imc:.1f}, com esse IMC a pessoa esta obesa.')
else:
    print(f'IMC: {imc:.1f}, com esse IMC a pessoa esta com obesidade mórbida.')