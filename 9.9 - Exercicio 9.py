#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

contMaiores = 0
contMenores = 0

for i in range (0, 7):
    anoNascimento = int(input('Insira seu ano de nascimento: '))
    if (2019 - anoNascimento) >= 18:
        contMaiores += 1
    else:
        contMenores += 1

print(f"""Ao todo tivemos {contMaiores} pessoas maiores de idade
E tambem tivemos {contMenores} pessoas menores de idade
""")