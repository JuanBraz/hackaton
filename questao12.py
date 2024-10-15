# Receber um valor em pés do usuario
pes = float(input('Digite um valor em pés: '))

# Tranformar o valor em polegadas, jardas e milhas
polegadas = pes * 12
jarda = pes / 3
milha = jarda * 1.76

print(f'O valor em polegadas é de {polegadas:.2f}')
print(f'O valor em jardas é de {jarda:.2f}')
print(f'O valor em milhas é de {milha:.2f}')