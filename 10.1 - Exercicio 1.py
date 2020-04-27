#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = str(input('Insira um sexo [M/F]: ')).strip().upper()
while sex not in 'FM':
    sex = str(input('Insira um sexo valido: ')).strip().upper()
    print('Sexo validado')