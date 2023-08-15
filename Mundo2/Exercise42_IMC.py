'''
Desenvolver uma logica que leia o peso e a altura de uma pessoa, calcular seu indice
de massa corporal(IMC) e mostrar seu status, de acordo com a tabela abaixo:
-IMC abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade Mórbida
'''
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'O seu IMC é de: {imc:.1f} = Abaixo do peso')

elif 18.5 <= imc < 25:
    print(f'O seu IMC é de: {imc:.1f} = Peso ideal')

elif 25 <= imc < 30:
    print(f'O seu IMC é de: {imc:.1f} == Sobrepeso')

elif 30 <= imc < 40:
    print(f'O seu IMC é de: {imc:.1f} === Obesidade')

else:
    print(f'O seu IMC é {imc:.1f} ======= Obesidade Mórbida')