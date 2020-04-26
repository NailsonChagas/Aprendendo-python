#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for i in range (1, 501):
    if i % 3 == 0:
        soma = soma + i
print(f'Soma dos numeros multiplos de 2 no intervalo: {soma}')

#ou

soma = 0
for i in range (3,501,3):
    soma = soma + i
print(f'Soma dos numeros multiplos de 2 no intervalo: {soma}')