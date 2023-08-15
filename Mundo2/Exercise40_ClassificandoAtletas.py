'''
Criar um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JÚNIOR
-Até 25 anos: SÊNIOR
-Acima de 25 anos: MASTER
'''
from datetime import date
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print(f'Você tem {idade}\nSua categoria é MIRIM')

elif 10 <= idade <= 14:
    print(f'Você tem {idade}\nSua categoria é INFANTIL')

elif 15 <= idade <= 19:
    print(f'Você tem {idade}\nSua categoria é JÚNIOR')

elif 20 <= idade <= 25:
    print(f'Você tem {idade}\nSua categoria é SÊNIOR')

else:
    print(f'Você tem {idade}\nSua categoria é MASTER')