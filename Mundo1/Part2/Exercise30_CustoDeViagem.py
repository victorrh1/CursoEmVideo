'''
Desenvolver um programa que pergunte a distancia de uma viagem em Km.
Calcular o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km.
E R$0,45 para viagens mais longas.
'''
viagem = float(input('Qual a distancia da viagem? '))
passagem = viagem * 0.50
passagem2 = viagem * 0.45
if viagem <= 200:
    print(f'Você vai viajar {viagem}Km\nSua passagem custará R${passagem:.2f}')

elif viagem > 200:
    print(f'Você vai viajar {viagem}Km\nSua passagem custará R${passagem2:.2f}')