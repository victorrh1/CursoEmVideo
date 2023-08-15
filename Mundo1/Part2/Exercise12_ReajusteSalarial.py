'''
Criar um algoritmo que leia o salario de um funcionario e mostre seu novo salario,
com 15% de aumento.
'''
salario = float(input('Qual é o salario do funcionario? R$'))
aumento = salario * 1.08

print('Um funcionario que ganhava R${}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salario, aumento))