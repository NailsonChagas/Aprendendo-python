# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Batata', 'Cenoura', 'Alface', 'Maracuja')

for palavras in tupla:
    print(f'As vogais da palavra {palavras.upper()} são: ', end='')
    for letras in palavras:
        if letras.lower() in 'aeiou':
            print(f'{letras} ', end='')
    print('')