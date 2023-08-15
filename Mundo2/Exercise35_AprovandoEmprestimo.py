'''
Criar um programa para aprovar o emprestimo bancario para a compra de uma casa.
1.Perguntar o valor da casa.
2.Salario do comprador.
3.Em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salario ou então o emprestimo será negado.
'''

valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salario do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))

valor_parcela = valor_casa / (financiamento * 12)
minimo = salario_comprador * 30 / 100
if valor_parcela <= minimo:
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {financiamento} anos')
    print(f'A prestação será de R${valor_parcela:.2f}')
    print(f'Emprestimo concedido')
else:
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {financiamento} anos')
    print(f'A prestação será de R${valor_parcela:.2f}')
    print(f'Emprestimo negado')