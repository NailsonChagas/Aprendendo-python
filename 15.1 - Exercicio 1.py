# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dicionario = dict()

dicionario['nome'] = str(input('Insira o nome: '))
dicionario['media'] = float(input('Insira a média: '))
if dicionario['media']>=7:
    dicionario['situacao'] = 'aprovado'
else:
    dicionario['situacao'] = 'reprovado'
for k,v in dicionario.items():
    print(f' - {k} é igual a {v}')
