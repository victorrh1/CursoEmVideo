'''
Criar um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e
tangente de angulo.
'''
from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
radian = radians(angulo)
seno = sin(radian)
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cos = cos(radian)
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
tan = tan(radian)
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))