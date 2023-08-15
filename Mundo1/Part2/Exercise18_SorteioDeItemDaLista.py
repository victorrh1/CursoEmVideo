'''
Criar um programa que ajude o professor a sortear um de seus quatro alunos para apagar o
quadro, mostrando o nome escolhido.
'''
from random import choice
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
alunos = [pa, sa, ta, qa]
escolhido = choice(alunos)
print('O aluno escolhido foi', escolhido)