nome = input('Qual é o seu nome\nR:')
idade = int(input('qual é a sua idade\nR:'))

print(f'O usuario digitou {nome}, '
      f'{nome} tem {idade} anos '
      f'tipo da variável é: {type(nome)}')

ano_nasc = 2021 - idade

print(f'{nome} tem {idade} anos \n'
      f'{nome} nasceu em {ano_nasc}')