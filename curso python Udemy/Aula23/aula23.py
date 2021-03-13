'''
for in em python
iterando String com for
função range(start = 0, stop, step = 1)
'''

nome = 'python'

for letra in nome:
    print(letra)

for numero in range(20, 10, -1):
    print(numero)

frase = 'python'
nova_frase = ''


for letra in frase:
    if letra == 't':
        nova_frase = nova_frase + letra.upper()
    elif letra == 'h':
        nova_frase += letra.upper()
    else:
        nova_frase += letra

print(nova_frase)