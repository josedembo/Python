'''
* Criar variáveis para nome (str), idade(int)
* altura (float) e peso (float) para uma pessoa
* criar variável com o ano atual
* obter o ano de nascimento de uma pessoa( baseado na idade e ano atual)
* obter o IMC da pessoa com duas casa decimais( baseado no peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-String com as chavas
'''
nome = 'José Dembo'
idade = 22
altura = 1.80
peso = 80.73
ano_actual = 2021
imc = peso/altura ** 2
ano_nasc = ano_actual-idade

print(f'{nome},tem {idade} anos, pesa {peso}kg, '
      f'seu ano de nascimento é {ano_nasc}, tem imc {imc:.2f}')

