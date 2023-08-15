'''
Criar um programa que pergunte o salario de um funcionario e calcular o valor do seu aumento.
Para salarios superiores a R$1250, calcular um aumento de 10%
Para salarios inferiores ou iguais, o aumento é de 15%
'''
salario_func = float(input('Qual é o salario do funcionario? R$'))
if salario_func > 1250 * 1.10:
    new_salary = salario_func * 1.10
    print(f'O seu salario era R${salario_func:.2f}\nCom o aumento passa a ganhar R${new_salary:.2f}')
elif salario_func <= 1250 * 1.15:
    new_salary = salario_func * 1.15
    print(f'O seu salario era R${salario_func:.2f}\nCom o aumento passa a ganhar R${new_salary:.2f}')