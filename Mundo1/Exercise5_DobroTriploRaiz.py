'''
Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
'''
n = int(input('Digite um numero: '))
n1 = n * 2
n2 = n * 3
r = n ** 0.5
print('O dobro de {} é {}, o triplo é {} e a raiz é {:.2f}'.format(n, n1, n2, r))