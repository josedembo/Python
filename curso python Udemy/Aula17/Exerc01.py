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