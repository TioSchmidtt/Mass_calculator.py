
print('------------------2017----------------')
print('  _____ __  __  _____                 ')
print(' |_   _|  \/  |/ ____|                ')
print('   | | | \  / | |         _ __  _   _ ')
print('   | | | |\/| | |        |  _ \| | | |')
print('  _| |_| |  | | |____    | |_) | |_| |')
print(' |_____|_|  |_|\_____|   | .__/ \__, |')
print('                         | |     __/ |')
print('                         |_|    |___/ ')
print('Calcule seu Indice de Massa Corporal ')
print('Criado Por Junior Schmidt v:1.0 ')
print('Insira apenas Numeros !!')

peso= float(input('--Informe Seu Peso:'))
a= float(input('--Informe Sua Altura:'))
ar=float (a ** 2)
imc=float (peso / ar)

print('O seu IMC é', imc, '!')
if imc < 18.5:
	print('Você está Abaixo do Peso')
elif imc > 18.6 and imc < 24.9:
	print('Você está no peso Ideal Parabéns')
elif imc > 25.0 and imc < 29.9:
	print('Levemente Acima do Peso ')
elif imc > 30.0 and imc < 34.9:
	print('Obesidade Grau I(Preucupante)')
elif imc > 35.0 and imc < 39.9:
	print('Obesidade Grau II(Severa)')
elif imc > 40:
	print('Obesidade Grau III(mórbida)')






