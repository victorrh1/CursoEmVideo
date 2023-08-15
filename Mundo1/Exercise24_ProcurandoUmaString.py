'''
Criar um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
'''
name = str(input('Digite um nome: '))
tem_silv = 'SILVA' in name.upper()
print('Tem Silva no nome?', tem_silv)