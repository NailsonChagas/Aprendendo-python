#Estrutura de condição if ... else
tempo = int(input('A quanto anos você usa esse carro?: '))
if tempo <= 3: #se tempo menor ou igual a 3
    print(f'Com {tempo} anos seu carro ainda é novo.')
else: #se não
    print(f'Com {tempo} anos seu carro já é velho.')
print('---------- Fim ----------')

#outra forma de fazer
tempo = int(input('\nA quanto anos você usa esse carro?: '))
print('Seu carro é novo'if tempo <=3 else 'Seu carro é velho')
print('---------- Fim ----------')

