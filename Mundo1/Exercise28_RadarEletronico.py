'''
Criar um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostrar uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por
cada Km acima do limite.
'''
carro = float(input('Qual foi a velocidade que o carro passou? '))
if carro > 80:
    valor_multa = (carro - 80) * 7 # valor da multa
    print(f'Você excedeu a velocidade permitida de 80Km/h\nO valor da multa é de R${valor_multa:.2f}')
    pontos = int((carro - 80) * 1) # pontos da cnh
    print(f'Você perdeu {pontos:.0f} ponto(s) na sua CNH')
elif carro >= 75: # Ultimo aviso de segurança
    print(f'Você está a {carro}Km/h, cuidado com o limite da via, tenha um Bom dia!')
else:
    print('Você está dentro do limite da via, tenha um Bom dia!')