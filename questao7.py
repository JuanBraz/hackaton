#Receber um valor em graus Fahrenheit
temperatura = int(input('digite o valor da temperatura em Fahrenheit: '))

#Tranformar em graus Celcius
celsius = 5/9*(temperatura - 32) 

print(f'o valor da temperatura em Celsius: {celsius:.2f}')