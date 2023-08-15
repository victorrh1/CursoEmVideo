'''
Criar um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o ultimo nome separadamente.
Ex:Ana Maria de Souza
Primeiro = Ana
Ultimo = Souza
'''
name = str(input('Digite o seu nome completo: ')).strip().split()
print('Prazer em te conhecer!')
print(f'O seu primeiro nome é {name[0]}')
print(f'O seu ultimo nome é {name[-1]}')