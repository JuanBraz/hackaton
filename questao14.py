#Receber o valor da base e altura do usuario
base = int(input('digite o valor da base: '))
altura = int(input('digite o valor da altura: '))

#Calcular perimetro area e diagonal
area = base * altura
perímetro = 2*(base + altura)
diagonal = (base**2 + altura**2)**0,5


print(f'o valor da area: {area}')
print(f'o valor do perímetro: {perímetro}')
print(f'o valor da diagonal: {diagonal}')