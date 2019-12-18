#leia um angulo e mostre seu seno, seu cosseno e sua tangente
from math import sin, cos, tan, radians
angulo = float(input('Insira um angulo: '))
print(f'Seno: {sin(radians(angulo)):.3f}  Cosseno: {cos(radians(angulo)):.3f}  Tangente: {tan(radians(angulo)):.3f}')

#sin, cos, tan só recebem valores em radianos