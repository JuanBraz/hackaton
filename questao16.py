# Receber um valor em peso
peso = int(input('digite seu peso: '))

# Calcular o novo peso caso ele ganhe peso ou perca
peso_ganho = peso*(15/100)
peso_perdido = peso*(20/100)
peso_gordura = peso + peso_ganho
peso_magro = peso - peso_perdido

print(f'A pessoa engordou: {peso_gordura:.2f}')
print(f'A pessoa emagreceu: {peso_magro:.2f}')