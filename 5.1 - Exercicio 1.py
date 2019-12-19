#receba o nome de uma pessoa e mostre ele om todas letras maiusculas , minusculas, quantas letras tem, quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print(f'Nome com todas letras maiusculas: {nome.upper()}')
print(f'Nome com todas letras minusculas: {nome.lower()}')

quantidadeAlgarismos = len(nome)
quantidadeDeEspaco = nome.count(' ')
nomeDividido = nome.split()
quantidadeLetrasPrimeiroNome = len(nomeDividido[0])
print(f'Quantidade de letras no nome: {quantidadeAlgarismos - quantidadeDeEspaco}')
print(f'Quantidade de letras do primeiro nome: {quantidadeLetrasPrimeiroNome}')