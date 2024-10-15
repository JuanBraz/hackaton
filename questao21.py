# Verificar se um número é divisivel ou não
def verifica_divisibilidade(a, b):
    if b == 0:
        print('divisao por zero  nao é permitida.')
    elif a% b == 0:
        print((f'{a} é divisivel por {b}'))
    else:
        print(f'{a} nao é divisivel por {b}')

a = int(input('digite o numero A: '))
b = int(input('digite o numero B: '))
verifica_divisibilidade(a, b)