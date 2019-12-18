n1 = input('Insira um numero:')
n2 = input('Insira outro numero:')
soma = n1 + n2 #nesse caso o + n aje como adição e sim como concatenação (juntar uma string a outra)
print(type(n1))
print(f'A soma vale {soma}')

numero1 = int(input('\nDigite um numero:')) #o dado recebido na variavel sera considerado um numero inteiro
numero2 = int(input('Digite outro numero:'))
soma2 = numero2 + numero1
print(type(numero1))
print(f'A soma vale {soma2}')

#tipos primitivos em python são int(1, 2, 3), float(7.2, 8.9, 3.14), bool (True, False), str(Frases, letras, simbolos)

numero1 = int(input('\nDigite um numero inteiro:'))
numero2 = int(input('Digite outro numero inteiro:'))
soma2 = numero1 + numero2
print(f'A soma entre {numero1} e {numero2} resulta em {soma2}') #outra forma de escrever: print('A soma entre {} e {} resulta em {}'.format(numero1, numero2, soma))

numero1 = float(input('\nDigite um numero:'))
print(numero1)
