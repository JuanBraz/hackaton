# Receber 3 valores do usuario 
num1 = float(input('Digite o prmeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

# Verificar qual dos 3 é o maior e o menor
menor = num1
maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f'O menor Número é {menor}')
print(f'O maior Número é {maior}')