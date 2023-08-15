'''
Criar um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
Pedir para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever se o usuario VENCEU ou PERDEU.
'''
from random import randint
num = int(input('Digite um numero: '))
num1 = randint(0, 5)
if num == num1:
    print(f'Você, VENCEU!\nO numero era: {num1}')
else:
    print(f'Você, PERDEU!\nO numero era: {num1}')