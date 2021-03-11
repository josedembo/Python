'''
Tabuada e calculadora
'''
sair_programa = 0
while sair_programa == 0:
    cal = 'Calculadora e Tabuada'
    print(f'{cal:=^40}')
    opcao = input('O programa a seguir  mostra a tabuada e possui uma pequena calculadora\n'
                  'digite:  \n(1) para calculadora  \n(2) para a tabuada \n(0)para sair do programa ')

    opcao = int(opcao)

    matriz = []
    soma = 0
    sub = 0
    mult = 0
    div = 0
    tamanho = 0
    if opcao == 1:
        qtd_valores = input('Você escoheu calculadora, quantos valores prentendes digitar ')
        qtd_valores = int(qtd_valores)
        while qtd_valores > 0:
            cont = 1
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
            x = 0
            sub = 0
            while x < tamanho:
                sub = sub + matriz[x]
            print(f'subtração = {sub}')
        elif sinal == '*':
            x = 0
            mult = 0
            while x < tamanho:
                mult = mult + matriz[x]
            print(f'multiplicaçao = {mult}')
        elif sinal == '/':
            x = 0
            div = 0
            while x < tamanho:
                div = div + matriz[x]
            print(f'divisão = {div}')
    elif opcao == 2:
        tab = input('informe a tabuada que pretende verificar: ')

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

