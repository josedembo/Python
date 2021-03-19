'''
for / else
'''
palavras = ['Frango', 'fernando', 'Eduardo']

'''
for palavra in palavras:
    if palavra.lower().startswith('f'):
        print(f'{palavra} começa com "f"')
    else:
        print(f'{palavra}, não começa com "f"')
'''

for palavra in palavras:
    if palavra.lower().startswith('f'):
        continue
    print(palavra)
else:
    print(f'não tem ´palavra que começa com "f"')