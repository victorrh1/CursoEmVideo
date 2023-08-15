'''
Criar um programa que leia duas notas de um aluno e calcule sua media,
mostrar uma mensagem no final, de acordo com a media atingida.
-Media abaixo de 5.0: Reprovado
-Media entre 5 e 6.9: Recuperação
-Media 7 ou superior: Aprovado
'''
p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
m = (p1 + p2) / 2
if m >= 7:
    print(f'A sua média é {m:.1f}\nParabéns, você foi \033[94mAPROVADO!\033[0m')

elif 5 <= m <= 6.9:
    print(f'A sua média é {m:.1f}\nEsforce-se mais, você está de \033[92mRECUPERAÇÃO\033[0m')

else:
    print(f'A sua média é {m:.1f}\nEstude mais e tente novamente, você foi \033[91mREPROVADO!\033[0m')