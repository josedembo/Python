'''
Tabuada e calculadora
'''
sair_programa = 0
while sair_programa == 0:
    cal = 'Calculadora e Tabuada'
    print(f'{cal:=^40}')
    opcao = input('O programa a seguir  mostra a tabuada e possui uma pequena calculadora\n'
                  'digite:  \n(1) para calculadora  \n(2) para a tabuada \n(0)para sair do programa ')
    if not opcao.isnumeric():
        print('Você precisa digitar um número')
        continue

    opcao = int(opcao)

    matriz = []
    soma = 0
    sub = 0
    mult = 0
    div = 0
    tamanho = 0
    if opcao == 1:
        qtd_valores = input('Você escolheu calculadora, quantos valores prentende digitar ')
        if not qtd_valores.isnumeric():
            print('Você precisa digitar um número')
            continue
        qtd_valores = int(qtd_valores)
        cont = 1
        while qtd_valores > 0:
            valor = input(f'informe o {cont}º valor ')
            valor = int(valor)
            matriz.append(valor)
            cont += 1
            qtd_valores -= 1
        sinal = input('informe o sinal da operacao, digite: \n(+) adicao '
                      '\n(-) subtracao \n(*) multiplicacao \n(/) para divisao')
        if sinal == '+':
            tamanho = len(matriz)
            x = 0
            soma = 0
            while x < tamanho:
                soma = soma + matriz[x]
                x += 1
            print(f'soma = {soma}')
        elif sinal == '-':
            tamanho = len(matriz)
            x = 0
            sub = 0
            while x < tamanho:
                if x == 0:
                    sub = sub + matriz[x]
                else:
                    sub = sub - matriz[x]
                x += 1
            print(f'subtração = {sub}')
        elif sinal == '*':
            tamanho = len(matriz)
            x = 0
            mult = 1
            while x < tamanho:
                mult = mult * matriz[x]
                x += 1
            print(f'multiplicaçao = {mult}')
        elif sinal == '/':
            tamanho = len(matriz)
            x = 0
            div = 0
            while x < tamanho:
                if x == 0:
                    div = div + matriz[x]
                else:
                    div = div / matriz[x]
                x += 1
            print(f'divisão = {div}')
    elif opcao == 2:
        tab = input('informe a tabuada que pretende verificar: ')
        if not tab.isnumeric():
            print('Você precisa digitar um número')
            continue

        if tab.isdigit():
            tab = int(tab)

        x = 1
        while x <= 12:
            result = tab * x
            print(f'{tab} * {x} = {result}')
            x += 1
    else:
        if opcao == 0:
            sair_programa = 1

