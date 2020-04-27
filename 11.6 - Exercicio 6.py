#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('========== CAIXA ELETRÔNICO ==========')

while True:
    valor = float(input('Insira o valor a ser sacado: R$'))

    cont50 = cont20 = cont10 = cont1 = 0

    cont50 = valor//50
    valor %= 50

    cont20 = valor // 20
    valor %= 20

    cont10 = valor // 10
    valor %= 10

    cont1 = valor // 1

    print(f'{cont50:.0f} notas de R$50, {cont20:.0f} notas de R$20, {cont10:.0f} notas de 10, {cont1:.0f} moedas de R$1, sobrando {(valor-(valor // 1))*100:.0f} centavos')
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()
    if escolha != 'S':
        break
    print('='*38)