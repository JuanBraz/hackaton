# Recebendo o valor do salario e do aumento
salario = (float(input('Digite o salario do funcionario: ')))
aumento = (int(input('Digite de quanto sera o aumento: ')))
# Calculando a porcentagem do aumento do salario
novosalario = aumento/100 * salario

print(f'O salario de {salario} com o aumento de {aumento}% será {novosalario}.')