#definindo a função: def nomeDaFunção(Parametros)
def mostraLinha():
    print('-'*18)
def soma(a,b):
    print(f'A:{a}  B:{b}')
    s = a+b
    print(s)
def criaTitulo(titulo):
    print('-'*30)
    print(titulo)
    print('-'*30)

mostraLinha()
criaTitulo('SISTEMA DE ALUNOS')
soma(1,3)
soma(b=3,a=9)

#Python pode empacotar parametros, quando uma vc n sabe quantos parametros uma função recebe  (* = desempacotar):
def contador(*numeros):
    print(numeros)
    for valor in numeros:
        print(valor, end='')
contador(1,2,3,4,5,6,7,8,9,11)