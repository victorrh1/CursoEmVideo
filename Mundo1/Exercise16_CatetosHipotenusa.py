'''
Criar um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triangulo. Calcular e mostrar o comprimento da hipotenusa.
'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))