# Verificar se o numero digitado pelo usuario e multiplo de 3
def verifica_multiplo_de_3(numero):
    if numero % 3 == 0:
        print(f'{numero} é multiplo de 3')
    else:
        print(f'{numero} nao é multiplo de 3')
    
numero = int(input('digite um numero: '))
verifica_multiplo_de_3(numero)
