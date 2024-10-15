# Recebendo o valor do salario base e da gratificação
salariobase = (float(input('Digite o salario base do funcionario: ')))
gratificacao = 50
# Calculando o imposto que vai ser descontado do salario
imposto = 10/100 * salariobase
# Calculando a adição do salario com a gratificação menos o imposto
salario = salariobase + gratificacao - imposto

print(f'O salario do funcionario com a gratificação de 50 reais e o desconto do imposto de 10% será {salario}.')