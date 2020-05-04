# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista =[[],[]]
for i in range(0,7):
    num = int(input(f'Insira o {i+1}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('-_'*16)
print(f'Os numeros pares são: {sorted(lista[0])}')
print(f'Os numeros impares são: {sorted(lista[1])}')