#exercicio 1: leia dois numeros e mostre a soma entre eles
numero1 = int(input('Insira o primeiro numero:'))
numero2 = int(input('Insira o segundo numero:'))
print(f'A soma entre {numero1} e {numero2} é {numero1+numero2}')

#exercicio 2: leia algo e mostre qual o seu tipo primitivo de dado
variavel = input('\nDigite algo: ')
print(f'Seu tipo primitivo é {type(variavel)}')
print(f'Só possui espaços: {variavel.isspace()}')
print(f'Ele é numerico: {variavel.isnumeric()}')
print(f'Ele é alfanumérico: {variavel.isalnum()}')
print(f'Ele é alfabético: {variavel.isalpha()}')
print(f'Tudo que foi digitado esta em maiusculo: {variavel.isupper()}')
print(f'Tudo que foi digitado esta em minusculo: {variavel.islower()}')
print(f'Esta Captalizada (primeira letra maiuscula): {variavel.istitle()}')


