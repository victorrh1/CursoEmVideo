'''
Desenvolver um sistema que leia o comprimento de 3 retas e diga para o usuario,
que tipo de triangulo será formado:
-EQUILÁTERO: sao iguais
-ISÓCELES: dois lados iguais
-ESCALENO: tudo diferente
'''
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 == seg2 == seg3:
    print('É UM EQUILATERO')

elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
    print('É UM ISOCELES')

elif seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print('É UM ESCALENO')

else:
    print('NÃO PODEM FORMAR UM TRIANGULO')