'''
Criar um programa em Python que leia um numero inteiro qualquer e peça para o usuario
escolher qual será a base de conversao:
1. Binario
2. Octal
3. Hexadecimal
'''

conversor = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversão:
    [ 1 ] Binário
    [ 2 ] Octal
    [ 3 ] Hexadecimal
    ''')

escolher = int(input('Sua opção: '))

if escolher == 1:
    print(f'{conversor} convertido para BINÁRIO é igual a {bin(conversor)[2:]}')

elif escolher == 2:

    print(f'{conversor} convertido para OCTAL é igual a {oct(conversor)[2:]}')
elif escolher == 3:

    print(f'{conversor} convertido para HEXADECIMAL é igual a {hex(conversor)[2:]}')
else:
    print('\033[91mNumero invalido!\033[0m')