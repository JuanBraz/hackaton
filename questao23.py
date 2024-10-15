# Calcular o IMC e verificar o Grau de obesidade do usuario
def calcular_IMC():
    peso= float(input('digite o peso (kg): '))
    altura= float(input('digite o altura (metros): '))

    IMC = peso/(altura **2)

    if IMC < 18.5:
        grau_obesidade ='Magreza' 
    elif 18.5 <= IMC <=24.9:
        grau_obesidade ='Saudavel'
    elif 25.0 <= IMC <=29.9:
        grau_obesidade ='Sobrepeso'
    elif 30.0 <= IMC <=34.9:
        grau_obesidade = 'obesidade Grau 1'
    elif 35.0 <= IMC <= 39.9:
        grau_obesidade = 'obesidade Grau 2'
    else:
        grau_obesidade = 'obesidade grau 3'

    print(f'Seu IMC é: {IMC:.2f}')
    print(f'grau de obesidade: {grau_obesidade}')

calcular_IMC()