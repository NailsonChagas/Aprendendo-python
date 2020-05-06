# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['anoNascimento'] = int(input('Ano de nascimento: '))
cadastro['idade'] = 2020 - cadastro['anoNascimento']
cadastro['carteiraDeTrabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['carteiraDeTrabalho'] != 0:
    cadastro['anoDeContratacao'] = int(input('Ano de crontratação: '))
    cadastro['aposentadoria'] = cadastro['anoDeContratacao'] + 35 - cadastro['anoNascimento']
    cadastro['salario'] = float(input('Salário: '))
for k,v in cadastro.items():
    print(f'{k} tem o valor {v}')