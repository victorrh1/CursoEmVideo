'''
Criar um sistema que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
'''
city = str(input('Em que cidade você nasceu? ')).strip()
city = city.upper()
print(city[0:5] == 'SANTO')