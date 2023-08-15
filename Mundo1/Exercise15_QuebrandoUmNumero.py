'''
Criar um programa que leia um numero Real qualquer e mostre a sua porção inteira.
'''
import math
numero = float(input('Digite um valor: '))
valor = math.floor(numero)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, valor))