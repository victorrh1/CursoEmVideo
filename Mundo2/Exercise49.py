'''
Criar um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconside-o.
'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o valor {c}: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A contagem dos números IMPARES {cont}\nA soma dos números PARES {soma}')