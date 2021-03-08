nome = 'José Dembo'
idade = 22
altura = 1.80
peso = 80.73
ano_actual = 2021
imc = peso/altura ** 2
ano_nasc = ano_actual-idade

print(f'{nome},tem {idade} anos, pesa {peso}kg, '
      f'seu ano de nascimento é {ano_nasc}, tem imc {imc:.2f}')