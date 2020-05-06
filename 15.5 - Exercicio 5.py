# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
lista = list()
listaMulher = list()
listaAcima = list()
i = 0
somaIdade = 0
while True:
    dicionario = dict()
    dicionario['Nome'] = str(input('Nome: '))
    dicionario['Sexo'] = str(input('Sexo[F/M]: ')).upper()
    dicionario['Idade'] = int(input('Idade: '))
    somaIdade += dicionario['Idade']
    i += 1
    lista.append(dicionario)
    if dicionario['Sexo'] == 'F':
        listaMulher.append(dicionario)
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()
    if escolha!='S':
        del dicionario
        for j in range(0,len(lista)):
            if lista[j]['Idade']>=18:
                listaAcima.append(lista[j])
        print('-=' * 18)
        break
    else:
        print('-='*18)
print(f'Foram cadastradas {i} pessoas')
print(f'A média de idade das pessoas cadastradas é: {somaIdade/i}')
print(f'Lista Mulheres: {listaMulher}')
print(f'Lista de pessoas acima da média: {listaAcima}')