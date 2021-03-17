'''
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
'''
lista = ['A','B','C']
lista_2 = ['A', 'B', 'C', 'E', 10.7]
nova_lista = lista[1:]
print(lista_2[::-2])

l1 = [4, 3, 6, 8]
l2 = [9, 6, 3]

l3 = l1 + l2
l1.extend(l2)
print(l1)
l1.insert(0, 20)
l1.insert(0, 'Hello word')
print(l1)
l1.pop()
print(l1)
del(l1[0])
print(l1)
del(l1[2])
print(l1)
print(max(l1))
print(min(l1))

soma = 0
for valor in l1:
    soma = soma + valor

print(f'soma = {soma}')
print(f'soma do max e min = {max(l1) + min(l1)}')

l = ['string', True, 6.8, 10]
for item in l:
    print(f'{item}', type(item))
