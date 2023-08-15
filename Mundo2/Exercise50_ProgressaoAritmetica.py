'''
Desenvolver um programa que leia o primeiro termo e a razão de uma Progressao Aritmetica.
No final, mostrar os 10 primeiros termos dessa progressao.
'''
PrimeiroT = int(input('Primeiro Termo: '))
Razao = int(input('Razão: '))
decimo = PrimeiroT + (10 - 1) * Razao
for c in range(PrimeiroT, decimo + Razao, Razao):
    print(c, end='-->')
print('FINISH')
