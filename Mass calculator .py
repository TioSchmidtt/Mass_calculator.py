
print('------------------2017----------------')
print('  _____ __  __  _____                 ')
print(' |_   _|  \/  |/ ____|                ')
print('   | | | \  / | |         _ __  _   _ ')
print('   | | | |\/| | |        |  _ \| | | |')
print('  _| |_| |  | | |____    | |_) | |_| |')
print(' |_____|_|  |_|\_____|   | .__/ \__, |')
print('                         | |     __/ |')
print('                         |_|    |___/ ')
print('calculate Your Body Mass Index ')
print('Created By Junior Schmidt brazil v: 1.0 ')
print('Enter only Numbers !!')

peso= float(input('- Report Your Weight in kg >>'))
a= float(input('- Report Your Height in cm >>'))
ar=float (a ** 2)
imc=float (peso / ar)

print('Your BMI is', imc, '!')
if imc < 18.5:
	print('You are underweight')
elif imc > 18.6 and imc < 24.9:
	print('You re at Ideal Weight Congratulations')
elif imc > 25.0 and imc < 29.9:
	print('Slightly Overweight')
elif imc > 30.0 and imc < 34.9:
	print('Obesity Grade I (Worrying)')
elif imc > 35.0 and imc < 39.9:
	print('Obesity Grade II (Severe)')
elif imc > 40:
	print('Obesity Grade III (morbid)')






