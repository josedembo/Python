'''
Laço while
abixo vemos um loop infinito
while True:
    nome = input('Qual é o seu nome? ')
    print(f'Olá {nome}')
'''
x = 0
while x <= 10:
    if x % 2 != 0:
        x +=1
        break
    print(x)
    x += 1
print('Acabou')

x1 = 0

while x1 < 10:
    y = 0
    while y < 5:
         print(f'x vale {x1}, y vale {y}')
         y += 1
    print('=' * 20)
    x1 += 1
print('acabou')