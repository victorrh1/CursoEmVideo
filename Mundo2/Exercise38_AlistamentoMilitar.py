'''
Criar um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
de se alistar ou se já passou do tempo do alistamento. O programa também deverá
mostrar o tempo que falta ou que passou do prazo.
1.Ano de nascimento
2.Condição: Se ele tem a idade necessaria para se alistar
3.Condição: Se ele já passou da idade para se alistar
4.Condição: Quanto tempo falta pra ele se alistar
'''
from datetime import date
# Perguntas
name = str(input('Qual é o seu nome? '))
sexo = str(input('Qual é o seu sexo? '))
nasc = int(input('Em que ano você nasceu? '))
# Variáveis
ano_atual = date.today().year
idade = ano_atual - nasc
# Condicionais + novas variáveis
if sexo.lower() == 'feminino':
    print(f'{name}, você não é obrigada a se alistar!')

elif idade >= 19:
    passou = idade - 18
    ano_alistamento1 = nasc + 18
    print(f'{name}, você tem {idade} ano(s), você deveria ter se alistado há {passou} ano(s) atrás')
    print(f'O seu ano de alistamento foi em {ano_alistamento1}')

elif idade >= 18:
    print(f'{name}, você tem {idade} ano(s), você deve se alistar IMEDIATAMENTE!')

else:
    ano_alistamento = 18 - idade
    ano_alistamento1 = nasc + 18
    print(f'{name}, você tem {idade} ano(s), você deverá se alistar daqui {ano_alistamento} ano(s)')
    print(f'O ano do seu alistamento será em {ano_alistamento1}')