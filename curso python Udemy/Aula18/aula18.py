'''
Formatação de valores com modificadores
'''
num1 = 1
num2 = 3
divisao = num1/num2

print('{:.1f}'.format(divisao))
print(f'{divisao:.2f}')

print(f'{num1:k<2}')