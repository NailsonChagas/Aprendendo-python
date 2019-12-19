#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Insira o nome de sua cidade: '))

cidadeDividida = cidade.split()

booleano = 'Santo' in cidadeDividida[0]

print(f'O nome da cidade começa com Santo: {booleano}')