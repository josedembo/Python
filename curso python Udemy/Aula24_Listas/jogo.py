import random
palavras = ['Wonderfull','Love','Felicidade','Porta','Prateado','Domingo','Destino']
secriword = random.choice(palavras)

digitadas = []

chances = 4
while True:
    if chances == 0:
        print(f'chances: {chances}')
        print('VOCÊ PERDEU')
        break
    else:
        print(f'chances: {chances}')
    letra = input('digite uma letra: ')
    if len(letra) > 1:
        print('Hooow! não vale, digite apenas uma letra')
        continue
    digitadas.append(letra)

    if letra in secriword:
        print(f'MUITO BOM, EXISTE a letra "{letra}"  na palavra secreta')
    else:
        print(f'HOOWW, a letra "{letra}", NÃO EXISTE na palavra secreta')
        digitadas.pop()
        chances -= 1

    n = len(secriword)
    secreta_temp = ''

    for letra_secreta in secriword:
        if letra_secreta in digitadas:
            secreta_temp += letra_secreta
        else:
            secreta_temp += '*'

    if secreta_temp == secriword:
        print(f'Que legal, você GANHOU, a palavra secreta é {secriword}')
        break
    else:
        print(f'a palavra secreta está assim: {secreta_temp}')
