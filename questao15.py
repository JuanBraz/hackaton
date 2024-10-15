#Receber o valor da prestação juros e tempo
valor_prestaçao = int(input('Digite o valor da prestaçao: '))
juros = float(input('Digite o valor do juros: '))
tempo = int(input('Digite o tempo em dias: '))

#Calculo da Prestação
taxa = juros/100
prestaçao = valor_prestaçao +( valor_prestaçao*(taxa/100)*tempo)

print(f'o calculo da prestaçao foi: {prestaçao}')

