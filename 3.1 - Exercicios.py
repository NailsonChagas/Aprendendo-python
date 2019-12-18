#leia um numero inteiro e mostre seu antecessor e seu sucessor
numero = int(input('Insira um numero: '))
print(f'O numero digitado foi {numero}, seu sucessor é {numero+1} e seu antecessor é {numero-1}')

#crie um algoritmo que leia um numero e mostre seu dobro, seu triplo e raiz quadrada
numero = int(input('\nInsira um numero: '))
print(f'O numero digitado foi {numero}, seu dobro é {numero*2}, seu triplo é {numero*3} e sua raiz quadrada é {(numero**(1/2)):.2f}')

#leias duas notas de um aluno e mostre a média
nota1 = float(input('\nInsira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
print(f'As notas do aluno são {nota1} e {nota2}, média: {(nota1+nota2)/2}')

#leia um valor em metros e o converta a centimetros e milimetros
medida = float(input('\nInsira um valor em metros: '))
print(f'O valor digitado foi {medida}m, {medida}m em centimetros é {medida*100}cm e em milimetros é {medida*1000}mm')

#leia um numero inteiro e exiba sua tabuada
numero = int(input('\nInsira um numero inteiro: '))
print(f'{numero} *  1 = {(numero * 1):>2}')
print(f'{numero} *  2 = {(numero * 2):>2}')
print(f'{numero} *  3 = {(numero * 3):>2}')
print(f'{numero} *  4 = {(numero * 4):>2}')
print(f'{numero} *  5 = {(numero * 5):>2}')
print(f'{numero} *  6 = {(numero * 6):>2}')
print(f'{numero} *  7 = {(numero * 7):>2}')
print(f'{numero} *  8 = {(numero * 8):>2}')
print(f'{numero} *  9 = {(numero * 9):>2}')
print(f'{numero} * 10 = {(numero * 10):>2}')

#coverta real pra dollar U$1.00 = R$3.27
dinheiro = float(input('\nQual a quantidade de R$ você possui?: '))
print(f'Com seus R${dinheiro} você pode comprar U${(dinheiro/3.27):.2f}')

#leia a altura e a largura de uma parede e dica quanto de tinta vc usara pra pintala (considerando que 1L pinta dois metros quadrados)
altura = float(input('\nInsira a altura (em metros) da sua parede: '))
largura = float(input('Insira a largura (em metros) da sua parede' ))
print(f'A parede tem area de {largura*altura}m^2 e para pintara ira gastar {(largura*altura)/2}L de tinta')

#leia o preço do produto e mostre o novo valor com um desconto de 5%
preco = float(input('\nQual o valor do produto?: '))
print(f'O valor com o desconto de 5% será de R${(preco-(preco*5/100)):.2f}')

#leia um salario e mostre seu salario com 15% de aumento
salario = float(input('\nQual o seu salario?: '))
print(f'O salario com 15% de aumento sera R${(salario+(salario*15/100)):.2f}')

#converter a temperatura de Celsius pra Kelvin e Fahrenheit
celsius = float(input('\nInsira a temperatura em C: '))
print(f'A temperatura em Fahrenheit é {(((9*celsius)/5)+32):.2f}F e em Kelvin é {(celsius+273.15):.2f}K')

#pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
kmPercorrido = float(input('\nKilometragem rodada pelo carro: '))
diasAlugado = int(input('Dias alugados: '))
custo = (kmPercorrido*0.15) + (diasAlugado*60)
print(f'O custo do alugue foi de R${custo:.2f}')

