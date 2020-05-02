#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
i = 0

while True:
    num = int(input(f'Insira o {i+1}º numero: '))
    if lista.count(num) == 0:
        lista.append(num)

    escolha = str(input('Deseja continuar a digitar numeros?[S/N]: '))
    i += 1

    if escolha in 'Ss':
        continue
    else:
        break

lista.sort()
print(f'Lista digitada em ordem crescente: {lista}')