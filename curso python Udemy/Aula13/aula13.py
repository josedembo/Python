'''
operadores lógicos: and, or, not
in, not in
'''
a = ''
b = 12
nome = 'José Dembo'
letra = 'mbo'

if not b:
    print('por favor preencha o valor de b')

if letra not in nome:
    print(f'Não Existe a letra {letra} no seu nome')
else:
    print(f'Existe a letra {letra} no seu nome')