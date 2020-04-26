#Escreva um programa em Python que leia um número inteiro qualquer
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('\n=============== CONVERSÃO DE BASES NUMÉRICAS ===============\n')
print('1: Inteiro -> Binário')
print('2: Inteiro -> Octal')
print('3: Inteiro -> Hexadecimal')
escolha = int(input('Qual a sua escolha: '))
print('============================================================\n')
if escolha == 1:
    print('Você escolheu a conversão Inteiro -> Binário')
    numero = int(input('Digite um número inteiro: '))
    print(f'(O numero {numero} em binário é: {bin(numero)})') #0b
elif escolha == 2:
    print('Você escolheu a conversão Inteiro -> Octal')
    numero = int(input('Digite um número inteiro: '))
    print(f'(O numero {numero} em binário é: {oct(numero)})') #0o
elif escolha == 3:
    print('Você escolheu a conversão Inteiro -> Hexadecimal')
    numero = int(input('Digite um número inteiro: '))
    print(f'(O numero {numero} em binário é: {hex(numero)})') #0x
else:
    print('ERRO: A opção escolhida não é valida!!!')