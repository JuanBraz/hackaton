# Verificar os dias da semana de acordo com o numro digitado
def dia_da_semana():
    numero = int(input('digite um numero entre 1 e 7: '))

    dias = {1:'domingo', 2:'segunda-feira', 3:'terça-feira', 4:'quarta-feira', 5:'quinta-feira', 6:'sexta-feira', 7:'sabado'}
    if numero in dias:
        print(f'O dia correspondente ao número {numero} é {dias[numero]}.')
    else:
        print('Nao existe dia da semana com esse numero.')

dia_da_semana()