'''
Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostrar quanto
ela pode comprar em dolares.
'''
carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
total = carteira / 3.27
print('Com R${} você pode comprar U${:.2f}'.format(carteira, total))