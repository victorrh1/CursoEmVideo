'''
Criar um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
'''
produto = float(input('Qual é o preço do produto? R$'))
desconto = produto * 5 / 100
novo_preco = produto - desconto
print('O produto custava R${}, na promoção com desconto de 5% vai custar {:.2f}'.format(produto, novo_preco))