'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
graus Farenheit.
'''
celsius = float(input('Informe a temperatura em °C: '))
farenheit = celsius * 9 / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(celsius, farenheit))