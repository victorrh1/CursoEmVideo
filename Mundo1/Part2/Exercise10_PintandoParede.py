'''
Criar um programa que leia a largura e a altura de uma parede em metros, calcular a sua
area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta
pinta uma area de 2 metros quadrados.
'''
dados = float(input('Largura da parede: ' ))
dados2 = float(input('Altura da parede: '))
area = dados * dados2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(dados, dados2, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))