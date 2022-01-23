# BMI Calculator

a = float(input('Enter your height in cm: '))
m = float(input('Enter your weight in kg: '))
h = float(a*0.01)

bmi = float(m//(h**2))
print('Your Body Mass Index is', bmi)