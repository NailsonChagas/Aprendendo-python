# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de
# um terreno retangular (largura e comprimento) e mostre a área do terreno.
def calculoAreaQuadrilatero(largura, comprimento):
    area = largura * comprimento
    return area
largura = float(input('Insira a largura (em metros) do terreno: '))
comprimento = float(input('Insira o comrimento (em metros) do terreno: '))
print(f'A área do terrano é de {calculoAreaQuadrilatero(largura,comprimento)}m²')