'''
Criar um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
'''
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[92m', end=' ')
        tot += 1
    else:
        print('\033[91m', end=' ')
    print(c, end=' ')
print(f'\n\033[93mO número {num}\nFoi divisivel por {tot} vezes\033[0m')
if tot == 2:
    print('\033[94mPRIMO\033[0m')
else:
    print('\033[91mNÃO é PRIMO\033[0m')
