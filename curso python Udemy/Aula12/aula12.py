'''
Operadores relacionais
== > >= < <= !=
'''
num1 = 2
num2 = 2
var_1 = 'José'
var_2 = 'Dembo'
print(num1, num2)
print(num1 == num2, type(num1), type(num2))
expressao = (num1 >= num2)
expressao_2 = var_1 != var_2

print(expressao)
print(expressao_2)

nome = input("Qual é o seu nome\nR:")
idade = (input(f'{nome}, qual é a sua idade\nR:'))
idade_limite = 18
idade = int(idade)
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, imprestimo concedido, Parabéns')
else:
    print(f'{nome}, imprestimo não concedido')