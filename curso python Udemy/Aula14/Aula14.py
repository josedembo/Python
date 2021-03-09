'''
quantidade de caracteres
'''
user = input('digite o seu usuario: ')
qtd_caractere = len(user)


if qtd_caractere < 8:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('usuario correto')

# print(user, qtd_caractere, type(qtd_caractere))

string1 = input('')
string2 = input('')

print(f'a quantidade total de caracteres digitado é: {len(string1) + len(string2)}')

print(string2.__len__())
print(len(string2))