#Faça um programa que leia um ano qualquer e diga se ele é bissexto
ano = int(input('Digite um ano: '))

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0): #and (e)/ or(ou), São bissextos todos os anos múltiplos de 400, são bissextos todos os múltiplos de 4 exceto se for múltiplo de 100 mas não de 400.
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
