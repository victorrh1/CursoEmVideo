'''
Criar um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:Numero: 3234
Unidade: 4
Dezena: 3
Centena: 2
Milhar: 3
'''
num = int(input('Informe um numero: '))
unidade = num % 10
print('A unidade é {}'.format(unidade))
dezena = (num % 100) // 10
print('A dezena é {}'.format(dezena))
centena = (num % 1000) // 100
print('A centena é {}'.format(centena))
milhar = num // 1000
print('O milhar é {}'.format(milhar))