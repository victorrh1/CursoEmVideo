'''
Desenvolver um programa que leia o comprimento de três retas e diga ao usuario se elas
podem ou não formar um triangulo
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('Os segmentos acima NAO podem formar um triangulo')