'''
Criar um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
'''
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
dias_alugado = dias * 60
km_rodados = km * 0.15
total = dias_alugado + km_rodados
print('O total a pagar é de R${:.2f}'.format(total))