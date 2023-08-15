'''
Criar um programa que leia e mostre o seu tipo primitivo e todas
as informações possiveis sobre ele.
'''
Info = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',(type(Info)))
print('Só tem espaço? ',Info.isspace())
print('É um numero? ',Info.isnumeric())
print('É alfabetico? ',Info.isalpha())
print('É alfa numerico? ',Info.isalnum())
print('Está em maiusculo? ',Info.isupper())
print('Está em minusculo? ',Info.islower())
print('Está capitalizada? ',Info.istitle())