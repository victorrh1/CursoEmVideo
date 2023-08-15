'''
Criar um programa que leia tres numeros e mostre qual é o maior e qual é o menor.
'''
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
# Verificação do valor maior
if (n1 > n2 and n1 > n3):
    print(f'O maior valor digitado foi {n1}')
elif (n2 > n1 and n2 > n3):
    print(f'O maior valor digitado foi {n2}')
elif (n3 > n1 and n3 > n2):
    print(f'O manior numero digitado foi {n3}')
# Verificação do valor menor
if n1 < n2 and n1 < n3:
    print(f'O menor valor digitado foi {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor valor digitado foi {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor valor digitado foi {n3}')
else:
    print(f'Os numeros digitados sao iguais, sendo assim não tem um menor ou maior ')