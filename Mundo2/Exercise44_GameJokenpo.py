'''
Criar um programa que faça jogar jokenpô
Pedra < Papel < Tesoura < Pedra
'''
from random import randint
start = str(input('Pressione "ENTER" para iniciar o jogo'))
print('''Jokenpô !
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
escolha = int(input('Qual será o número escolhido? '))

opcao = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
print('Você escolheu:', opcao[escolha])

maquina = randint(1, 3)
print('O PC escolheu', opcao[maquina])

if escolha == maquina:
    print('Deu Empate !')

elif (escolha == 1 and maquina == 3) or (escolha == 2 and maquina == 1) or (escolha == 3 and maquina == 1):
    print('Voce GANHOU !')

else:
    print('Voce PERDEU !')
