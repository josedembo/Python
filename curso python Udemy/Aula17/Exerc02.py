hora = input('Que horas são?')

try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom Dia')
    else:
        if hora >= 12 and hora <= 17:
            print('Boa Tarde')
        else:
            if hora >= 18 and hora <=23:
                print('Boa Noite')
except:
    print('Erro')