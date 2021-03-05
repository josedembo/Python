import random

cidades = ['Sao Paulo', 'Ceara', 'Recife',
           'Alagoas', 'Rio Grande do Sul', 'Rio de Janeiro']
numeros = [1, 45, 100, 19, 519, 200]
tentativas = 0

while tentativas < 2:

    print('================JOGO DA SORTE======================\n')
    print('seja bem-vido\n')
    print('======Nota: O jogo funciona da sguinte forma, podes escolher entre acertar cidade, ou um numero especifico=====')
    print('=======Voce tem apenas dua opcoes tanto para cidades ou numero da sorte\n')
    print('As cidades sorteadas  sao:\n')

    print('=====(1)Sao Paulo\n=====(2)Ceara\n=====(3)Recife\n=====(4)Alagoas\n=====(5)Rio Grande do Sul\n=====(6)Rio de Janeiro\n')
    print('Os numeros sao:\n===== 1\n===== 45\n===== 100\n===== 19\n===== 519\n===== 200\n')

    if tentativas ==0:
        nome = input('Informe o seu nome\nR:')

    tipo_de_jogo =int(input('qual o tipo e sorteio que você pretende jogar? \ndigite 1 para cidade da Sorte ou 2 para numero da sorte'))

    if tipo_de_jogo == 1:
        cidade_escolhida = int(input('escolha a cidade'))
        cidade_certa = random.choice(cidades)
        if cidade_certa == cidades[cidade_escolhida-1]:
            print(nome, 'Voce venceu o jogo')
            print('cidade sorteada:', cidade_certa)
        else:
            print(nome, 'Infelizmente você não venceu')
            print('cidade sorteada:', cidade_certa)
    else:
        numero_escolhido = int(input('escolha um número'))
        numero_certo = random.choice(numeros)
        if numero_escolhido == numero_certo:
            print(nome, 'Você venceu o jogo')
            print('numero  sorteado:', numero_certo)
        else:
            print(nome, 'Infelizmente você não venceu')
            print('numero sorteado:', numero_certo)
    tentativas += 1
