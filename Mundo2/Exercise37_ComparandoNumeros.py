'''
Criar um programa que leia dois numeros inteiros e compare-os.
Monstrando-os uma mensagem
1.O primeiro valor é maior
2.O segundo valor é maior
3.Não existe valor maior, os dois são iguais
'''
p1 = int(input('Digite o primeiro valor: '))
p2 = int(input('Digite o segundo valor: '))
if p1 > p2:
    print(f'O Primeiro valor {p1} é maior')
elif p2 > p1:
    print(f'O Segundo valor {p2} é maior')
else:
    print('Não existe valor maior, os dois são iguais')