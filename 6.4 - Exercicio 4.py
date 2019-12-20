#receba a distancia de uma viagem em km, calcule o preço da viagem, cobrado R$00,50 por km  para viagens de até 200Km e R$00,45 para viagens mais longas
kilometragem = float(input('Insira quantos kilometros serão percorridos na viagem: '))

if kilometragem <= 200:
    print(f'O custo da viagem de {kilometragem}Km será de R${(kilometragem * 0.50) :.2f}')
else:
    print(f'O custo da viagem de {kilometragem}Km será de R${(kilometragem * 0.45) :.2f}')
