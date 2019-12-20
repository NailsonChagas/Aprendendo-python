#leia a velocidade de um carro, se ele ultrapassar 80Km/h fale que ele foi multado A multa vai custar R$7,00 por cada Km acima do limite
velocidade = float(input('Qual a velocidade do carro (em Km/h)?: '))
multa = velocidade - 80

if multa <= 0:
    print(f'Á {velocidade}Km/h seu carro esta na faixa de velocidade permitida.')
else:
    print(f'Como seu carro esta á {velocidade}Km/h você esta sendo multado no valor de R${(multa*7):.2f}')