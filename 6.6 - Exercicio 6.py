#leia 3 numeros e mostre qual é o maior e qual é o menor
numero1 = int(input('Insira o numero 1: '))
numero2 = int(input('Insira o numero 2: '))
numero3 = int(input('Insira o numero 3: '))

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

if maior > numero3:
    if menor > numero3:
        menor = numero3
else:
    maior = numero3



print(f'O numero {maior} é o maior e o numero {menor} é o menor')