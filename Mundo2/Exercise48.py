'''
Refazer o desafio 9, mostrando a tabuada de um numero que o usuario escolher, só que agora
utilizando o laço for.
'''
from time import sleep
num = int(input('Digite um numero para saber a tabuada: '))
print(f'A tabuada de {num} é:')
for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
        sleep(1)
