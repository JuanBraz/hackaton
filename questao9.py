# Declaração da variaveis
cateto1 = float(input('Digite um valor pro primeiro cateto: '))
cateto2 = float(input('Digite um valor pro segundo cateto: '))

# Calculo da para identicar o valor da hipotenusa
hipotenusa = (cateto1**2 + cateto2**2)**0.5

print(f'O valor da hipotenusa é de {hipotenusa:.2f}')