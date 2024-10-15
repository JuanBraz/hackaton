# Receber a letra digitada pelo usuario
letra = input('Digite uma letra: ')
letra = letra.lower()

# Verificar se é uma vogal ou consoante
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Letra é uma vogal')
else:
    print('Letra é uma consoante')