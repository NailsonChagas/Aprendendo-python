#Escreva um programa que force o computador pensar em um numero entre 0 e 5 e tente adinivaar qual foi
from random import randint #randint (gera um numero inteiro aleatório)
from playsound import playsound

numeroRand = randint(0,5) #randint(0,5) vai geran um numero entre 0 e 5
numeroUsuario = int(input('Qual numero de 0 a 5 você acha que foi sorteado?: '))

if numeroUsuario == numeroRand:
    print(f' Parabéns, {numeroRand} foi o numero sorteado!!!')
    playsound('som de moeda.mp3')
else:
    print(f'Infelizmente o numero sorteado foi {numeroRand} e não {numeroUsuario}.')
    playsound('Game Over.mp3')