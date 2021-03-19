'''
split, join, enumerate em python
split: dividir uma string
join: juntar uma string ou lista
enumerate: enumerar elementos da lista #interavel
'''
string = 'Brasil é o país do futebool, brasil é o penta penta penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra_rep = ''
contagem = 0
qtd = 0
for palavra in lista_1:
    # print(f'a palavra "{palavra}" aparece  {string.count(palavra)}x na frase')
    qtd = string.count(palavra)

    if qtd > contagem:
        contagem = qtd
        palavra_rep = palavra
print(f'A palavra mais repetida é: {palavra_rep}, aparece {contagem}x')

for valor in lista_2:
    print(valor.strip().capitalize()) # a funçaõ strip remove os espaços no
    # inicio e fim de uma string

print(lista_1)
print(' '.join(lista_1)) # a função join transforma uma lista em string