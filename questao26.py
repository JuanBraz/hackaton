# Verificar o a quantidade de letras da palavra inserida pelo usuário
def verifica_paridade_palavra(palavra):
    quantidade_letras = len(palavra)
    if quantidade_letras %2 == 0:
        print(f'a palavra {palavra} tem {quantidade_letras} letras, que é um numero par.')
    else:
        print(f'a palavra {palavra} tem {quantidade_letras} letras, que é um numero impar')

palavra = input('digite uma palavra: ')
verifica_paridade_palavra(palavra)