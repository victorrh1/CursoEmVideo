'''
Desenvolver um programa que leia um valor em metros e o exiba convertido em centimentros,
milimetros, hectometro, decametro, decimetro, quilometro.
'''
medida = float(input('Uma distândcia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.1f}m corresponde a:\n{}km\n{}hm\n{}dam\n{}dm\n{:.0f}cm\n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))