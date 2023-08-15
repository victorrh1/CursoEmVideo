'''
Criar um programa que leia o nome completo de uma pessoa e mostre:
1.O nome com todas as letras maiusculas.
2.O nome com todas as letras minusculas.
3.Quantas letras ao todo(sem considerar espaços).
4.Quantas letras tem o primeiro nome.
'''
nc = str(input('Digite seu nome completo: '))
print('Analisando seu nome...\nSeu nome em maiúsculas é {}'.format(nc.upper()))
print('Seu nome em minúsculas é {}'.format(nc.lower()))
nc_nospace = nc.replace(' ', '')
print('Seu nome tem ao todo {} letras'.format(len(nc_nospace)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nc.split()[0], len(nc.split()[0])))