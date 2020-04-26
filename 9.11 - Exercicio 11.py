#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadeTotal = 0
nomeHomemMaisVelho = ''
contMulher = 0
maiorIdade = 0

for i in range (0,4):
    print(f'---------- {i+1}ª PESSOA ----------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if sexo == 'M' and idade > maiorIdade:
        nomeHomemMaisVelho = nome
        maiorIdade = idade

    idadeTotal += idade

    if sexo == 'F' and idade < 20:
        contMulher += 1

print(f'A média de idade do grupo é de {idadeTotal/4} anos')
print(f'O homem mais velho do grupo tem {maiorIdade} anos e se chama {nomeHomemMaisVelho}')
print(f'Ao todo são {contMulher} mulheres com menos de 20 anos')