'''
Criar um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
ainda não atingiram a maioridade e quantas ja sao maiores.
'''
atingiram = 0
nao_atingiram = 0
from datetime import date
for c in range(1, 8):
    pessoas = int(input(f'Pessoa nº{c}: '))
    data_atual = date.today().year
    ano_nasc = data_atual - pessoas
    if ano_nasc >= 18:
        atingiram += 1
        print(f'A Pessoa n°{c} ATINGIU a MAIORIDADE\nA idade atual é {ano_nasc}')
    else:
        nao_atingiram += 1
        print(f'A Pessoa n°{c} NÃO ATINGIU a MAIORIDADE\nA idade atual é {ano_nasc}')
