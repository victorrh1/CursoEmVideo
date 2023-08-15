'''
Criar um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''
produto = float(input('Digite o valor do produto:R$ '))
print('''[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: Preço normal
[ 4 ] Em 3x ou mais no cartão: 20% de juros
''')
vezes = int(input('Como deseja realizar o pagamento? '))
# Variaveis
desconto_money = produto - produto * (10 / 100)
desconto_card = produto - produto * (5 / 100)
juros = produto * (1 + 0.20)
# Condicionais
if vezes == 1:
    print(f'O produto custará R${desconto_money:.2f}, tendo um desconto de 10%')

elif vezes == 2:
    print(f'O produto custará R${desconto_card:.2f}, tendo um desconto de 5%')

elif vezes == 3:
    parcela = produto / 2
    print(f'O produto parcelado em 2x, custará R${produto:.2f}, com parcelas de R${parcela:.2f} cada')

else:
    jcard = int(input('Em quantas vezes será parcelado? '))
    parcelas = juros / jcard
    print(f'O produto parcelado em {jcard}x, custará R${juros:.2f}, com parcelas de R${parcelas:.2f} cada')