# Receba um número e exiba se ele é positivo ou negativo

numero = float(input('Digite um número: '))

if numero > 0:
    print(f'O número é positivo. {numero}')
elif numero == 0:
    print(f'O número é neutro. {numero}')
else:
    print(f'O número é negativo. {numero}')