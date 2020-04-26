#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

idade = int(input('Qual a idade do atleta: '))

if idade <= 9:
    print(f'Com a idade de {idade} anos, o atleta é classificado na categoria MIRIM.')
elif idade>9 and idade<=14:
    print(f'Com a idade de {idade} anos, o atleta é classificado na categoria INFANTIL.')
elif idade>14 and idade<=19:
    print(f'Com a idade de {idade} anos, o atleta é classificado na categoria JÚNIOR.')
elif idade>19 and idade<=25:
    print(f'Com a idade de {idade} anos, o atleta é classificado na categoria SÊNIOR.')
elif idade>25:
    print(f'Com a idade de {idade} anos, o atleta é classificado na categoria MASTER.')
else:
    print('A idade digitada é invalida.')