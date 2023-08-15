'''
Criar um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
os espaços.
EX: Apos a sopa, A sacada da casa, A torre da derrota, O Lobo ama o bolo, Anotaram a data da maratona
'''
word = str(input('Digite uma frase: ')).strip().upper()
palav = word.split()
junto = ''.join(palav)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('PALINDROMO')
else:
    print('NÃO é PALINDROMO')

# Sem o for

'''frase = input('Digite uma frase: ').strip().upper()
word = frase.split()
junto = ''.join(word)
inverso = junto[::- 1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('PALINDROMO')
else:
    print('NÃO é PALINDROMO')
'''
