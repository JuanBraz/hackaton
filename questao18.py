# Receber o valor da distancia da viagem, o carro utilizado e o preço do combustivel
percurso = float(input('digite o percurso da viagem em km: '))
tipo_carro = input('Digite o tipo do carro utilizado (A,B ou B): ').upper()
preco_combustivel = float(input('digite o preço do litro do combustivel (em reais): '))

# Verificação do consumo de combustivel e custo da viagem
if tipo_carro == 'A':
    consumo = percurso/16 
elif tipo_carro == 'B':
    consumo = percurso/12
elif tipo_carro == 'C':
    consumo = percurso/8
else:
    consumo = None 
    print('nao existe esse carro')
if consumo is not None:
    custo_viagem= consumo*preco_combustivel
        
print(f'consumo estimado de combustivel: {consumo:.2f} listros')  
print(f'valor estimado da viagem: R${custo_viagem:.2f}')
