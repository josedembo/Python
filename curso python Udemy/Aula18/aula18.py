'''
Formatação de valores com modificadores
'''
num1 = 1
num2 = 3
nome = 'José Dembo'
divisao = num1/num2

print('{:.1f}'.format(divisao))
print(f'{divisao:.2f}')

# formatando numeros com f-Strings (f'')
print(f'{num1:0>6}')
print(f'{num2:0>10.3f}')
print(num2, type(num2))

# formatando strings com f-Strings (f'')
menu ='Menu'
print(len(menu))
print(f'{menu:=^24}')

# formatando nome com .format

nome2 = 'José Pedro Daniel Dembo'
print(len(nome2))
nome2_formatado = '{a:@>30}, {a}, {a}'.format(a=nome2)
variaveis = '{0:0>11}, {1:0<11}, {2:#^30}, {3:@^100}'.format(num1,num2,nome, nome2)

print(nome2_formatado,"\n",variaveis)