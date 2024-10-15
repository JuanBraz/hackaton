# Recebendo o valor das horas trabalhadas e do salario minimo
horastrabalhadas = (int(input('Digite a quantidade de horas trabalhadas: ')))
salariominimo = (float(input('Digite o valor do salario minimo: ')))
valorhora = salariominimo/2
# Calculando a multiplicação das horas trabalhadas pelo valor da hora
salariobruto = horastrabalhadas * valorhora
# Calculando o imposto que vai ser descontado do salario
imposto = 3/100 * salariobruto
# Calculando a subtração do salario bruto com o imposto
salario = salariobruto - imposto

print(f'O salario do funcionario com o desconto do imposto de 3% é {salario}.')
