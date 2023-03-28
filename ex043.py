peso = float(input('Qual seu peso? (kg) '))
alt = float(input('Qual sua altura? (m) '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print(f'Você está abaixo do peso, seu IMC é {imc:.2f}.')
elif 18.5 <= imc < 25:
    print(f'Peso ideal, seu IMC é {imc:.2f}.')
elif 25 <= imc < 30:
    print(f'Você está em sobre peso, seu IMC é {imc:.2f}.')
elif 30 <= imc < 40:
    print(f'Você está com obesidade, seu IMC é {imc:.2f}.')
elif imc >= 40:
    print(f'Você está com obesidade mórbida, seu IMC é {imc:.2f}.')
