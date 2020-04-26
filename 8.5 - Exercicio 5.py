#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

print('\n===================== MÉDIA DOS ALUNOS =====================')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print('============================================================')

media = (nota1+nota2)/2

if media<5:
    print(f'Nota: {media:.2f}, aluno reprovado.')
elif media>5 and media<6.9:
    print(f'Nota: {media:.2f}, aluno de recuperação.')
else:
    print(f'Nota: {media:.2f}, aluno aprovovado')