# Receber um valor maiorque 0 do usuário
num1 = int(input('Digite um número maior que 0: '))

# Elevar esse valor ao quadrado e ao cubo e mostrar sua raiz quadrada e cúbica 
quadrado =  num1 ** 2
cubo = num1 ** 3
raiz_quadrada = num1 ** (1/2)
raiz_cubica = num1 ** (1/3)


print(f'O valor do numero ao quadrado é de{quadrado}')
print(f'O valor do numero ao cubo é de {cubo}')
print(f'O valor do numero na raiz quadrada é de {raiz_quadrada}')
print(f'O valor do numero na raiz cubica é de {raiz_cubica}')