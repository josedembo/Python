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

l1 = [4,3,6,8]
l2 = [9,6,3]

l3 = l1 + l2
l1.extend(l2)
l1.insert(0, 20)
print(l3)
print(l1)