'''
Exercicios propostos
'''

numero = input('informe um numero ')

try:
    numero = int(numero)
    if numero % 2 == 0:
        print('O numero digitado e par')
    else:
        print('O numero digitado nao e par')
except:
    print('ERRO')

'''   
if not numero.isdigit():
    print(f'{numero} não é um número inteiro')
else:
    numero = int(numero)
    if not numero % 2 == 0:
        print(f'{numero} é ímpar')
    else:
        print(f'{numero} é par')
'''