#Primeiros comandos

print('Olá mundo')
print(7 + 4)
print('7 + 4')
print('7' + '4') #7 e 4 não são numeros e s strings
print('Setenta' + 'Quatro')
print('Ola: ', 4) #ola é uma string e 4 é um numero

nome = 'Nailson'
idade = 19
print('Nome:', nome, 'Idade:', idade)


nomeRecebe = input('Qual o seu nome?: ')
idadeRecebe = input('Qual a sua idade?: ')
print('Nome:', nomeRecebe, 'Idade:', idadeRecebe)


dia = input('Qual o dia de hoje?: ')
mes = input('Qual o mês atual?: ')
ano = input('Em que ano estamos?: ')
print('Hoje o dia é', dia, 'do mês de', mes, 'e ano', ano)

numero1 = input('Insira um numero: ')
numero2 = input('Insira outro numero: ')
print('A soma efetuada da forma errada é:', numero1 + numero2) #soma as duas variaveis como se fossem strings

soma = numero1 + numero2
print('Soma teste', soma) #soma as duas variaveis como se fossem strings

soma = int(numero1) + int(numero2) #necessario informar qual o tipo de valor que a variavel armazena
print('Soma feita de forma correta: ', soma)

nome = input('Qual seu nome?: ')
print('Seu nome é {}!'. format(nome))
#ou ainda
print(f'Seu nome é {nome}!')
