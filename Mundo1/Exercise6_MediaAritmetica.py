'''
Desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
'''
nota = float(input('Digite a sua nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
n = nota + nota2
m = n / 2
print('A média entre {} e {} é igual a {:.1f}'.format(nota, nota2, m))