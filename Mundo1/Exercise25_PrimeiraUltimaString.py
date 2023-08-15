'''
Criar um programa que leia uma frase pelo teclado e mostre:
1.Quantas vezes aparece a letra "A"
2.Em que posição ela aparece pela primeira vez
3.Em que posição ela aparece a ultima vez
'''
name = str(input('Digite um nome: ')).upper().strip()
print('A letra A aparece {} vezes'.format(name.count('A')))
print('A letra A aparece na posição {}'.format(name.find('A') + 1))
print('A letra A sua ultima posição {}'.format(name.rfind('A') + 1))