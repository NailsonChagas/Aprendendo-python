#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('\n================= ALISTAMENTO MILITAR =================')
anoNascimento = int(input('Qual seu ano de nascimento: '))
print('=======================================================\n')

anoAtual = 2019
idade = anoAtual - anoNascimento

print(f'No ano de {anoAtual} você tera {idade} anos.')

if idade > 18:
    print(f'Seu alistamento esta atrasado, você deveria ter se alistado a {idade-18} anos.')
elif idade < 18:
    print(f'Você não precisa se alistar ainda, seu alistamneto obrigatório sera daqui {18-idade} anos.')
else:
    print('Você ira fazer 18 anos neste ano, você precisa se alistar agora.')