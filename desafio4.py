# Recebendo o valor do salario
salario = (float(input('Digite o salario do funcionario: ')))
# Calculo da porcentagem do aumento
aumento = 25/100 * salario
# Calculando a adição do salario com o aumento
novosalario = salario + aumento

print(f'O salario com o aumento de 25% é {novosalario}')