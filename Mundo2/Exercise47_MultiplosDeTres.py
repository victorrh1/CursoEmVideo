'''
Criar um programa que calcule a soma entre todos os numeros impares que são multiplos de três
e que se encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'O valor total: {soma} a contagem foi de: {cont} numeros')
