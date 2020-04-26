#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

print('=================== PALINDROMO ===================')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
fraseJunta = ''.join(palavras)

inverso = ''

for letra in range (len(fraseJunta)-1, -1, -1): #len = tipo letra
    inverso += fraseJunta[letra]

if fraseJunta == inverso:
    print('A frase digitada é um palindromo')
else:
    print('A frase digitada não é um palindromo')