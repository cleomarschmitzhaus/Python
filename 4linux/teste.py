# Decisões alinhadas ou decisões em sequencia
# Calculo do IMC

# 1 capturar as informações de peso e altura
peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))

# 2 Calcular o indice do IMC
imc = peso / (altura ** 2)

# 3 Classificar o IMC
if imc < 18.5:
    print(f'Baixo Peso - IMC: {imc:.2f}') #f = strg # formatação de numeros depois do 0 ":.2f"
elif imc < 24.9:
    print(f'Normal - IMC: {imc:.2f}')
elif imc <29.9:
    print(f'Pré obesidade - IMC: {imc:.2f}')
elif imc < 34.9:
    print(f'Obesidade Grau I - IMC: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade grau II - IMC: {imc:.2f}')
else:
    print(f'Obesidade grau III - IMC: {imc:.2f}')

# Numero de classificações - 1 -> de 6 Valida 5 e cai na ultima caso necessário

exit()