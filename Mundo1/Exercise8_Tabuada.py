'''
Criar um programa que leia um numero inteiro qualquer e mostre a sua tabuada.
'''
tabuada = int(input('Digite um numero para ver a sua tabuada: '))
n1 = tabuada * 1
n2 = tabuada * 2
n3 = tabuada * 3
n4 = tabuada * 4
n5 = tabuada * 5
n6 = tabuada * 6
n7 = tabuada * 7
n8 = tabuada * 8
n9 = tabuada * 9
n10 = tabuada * 10
print('------------\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}'.format(tabuada, n1, tabuada, n2, tabuada, n3, tabuada, n4, tabuada, n5))
print('{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}\n------------'.format(tabuada, n6, tabuada, n7, tabuada, n8, tabuada, n9, tabuada, n10))

#Other ex:

num = int(input('Digite um numero para gerar uma tabuada: '))
print('-'*12)
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('-'*12)