#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

cont18 = 0
contMen = 0
contFem20 = 0
s = ''
while True:
    idade = int(input('Insira a idade: '))

    sexo = str(input('Insira o genero [F/M]: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        if idade > 18:
            cont18 += 1
        if sexo == 'M':
            contMen += 1
        elif sexo == 'F' and idade < 20:
            contFem20 += 1
    else:
        print(f'Insira um genero valido, você digitou {sexo}')
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Insira o genero [F/M]: ')).strip().upper()

    s = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if s == 'N':
        print('-=-' * 11)
        break
    else:
        print('-=-'*11)

print(f'{cont18} pessoas tem mais de 18 anos')
print(f'{contMen} homens foram contados')
print(f'{contFem20} mulheres tem menos de 20 anos')
