'''
Usuário login
'''
user = input('informe o usuário ')
password = input('digite a senha ')

user_bd = 'josedembo'
password_us = '123456'

if user == user_bd and password == password_us:
    print('login feito com sucesso')
else:
    print('usuario ou senha inválida')