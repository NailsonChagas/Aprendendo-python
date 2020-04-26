#and = e / or = ou
#else if (em C)= elif

numero1 = int(input('Insira um numero: '))
numero2 = int(input('Insira outro numero: '))

if numero1 > numero2:
    print(f'Como {numero1} > {numero2} a soma entre eles é {numero1+numero2}')
elif numero1 == numero2: #else if
    print('Os numeros digitados são iguais.')
elif numero1 < numero2:
    print(f'Como {numero1} < {numero2} a diferença entre eles é {numero1-numero2}')
else:
    print('Fora das condições acima.')