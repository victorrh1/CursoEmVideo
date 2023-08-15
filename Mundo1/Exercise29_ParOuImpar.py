'''
Criar um programa que leia um numero inteiro e mostrar se ele é PAR ou IMPAR.
'''
num = int(input('Digite um numero: '))
if num % 2 == 0:
    print(f'O numero {num} é PAR')
else:
    print(f'O numero {num} é IMPAR')