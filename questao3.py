import random

print('Medico - Jornalista - Advogado - Professor - Físico - Comerciante - Estudante')
input('Tecle enter para sorteas sua profissao: ')

profissao = random.randint(1,7)

if profissao == 1:
    print('Sua prodissão é medico')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade:')    
    if escolha == 'A' or escolha == 'a':
        print(20*50 + 10*25)
    else:
        print(20*50 + 5*25)

elif profissao == 2:
    print('Sua prodissão é Jornalista')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade:')    
    if escolha == 'A' or escolha == 'a':
        print(20*24 + 10*12)
    else:
        print(20*24 + 5*12)

elif profissao == 3:
    print('Sua prodissão é Advogado')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade:')    
    if escolha == 'A' or escolha == 'a':
        print(20*50 + 10*25)
    else:
        print(20*50 + 5*25)

elif profissao == 4:
    print('Sua prodissão é Professor')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade:')    
    if escolha == 'A' or escolha == 'a':
        print(20*24 + 10*12)
    else:
        print(20*24 + 5*12)

elif profissao == 5:
    print('Sua prodissão é Físico')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade:')    
    if escolha == 'A' or escolha == 'a':
        print(20*30 + 10*15)
    else:
        print(20*30 + 5*15)

elif profissao == 6:
    print('Sua prodissão é Comerciante')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade:')    
    if escolha == 'A' or escolha == 'a':
        print(20*12 + 10*6)
    else:
        print(20*12 + 5*6)

elif profissao == 7:
    print('Sua prodissão é Estudante')
    escolha = input('Digite seu camaniho \nA- para receber 30x seu salario, mas 10 serão pagos pela metade:: \nB- para receber 25x seu salario, mas 5 serão pagos pela metade::')    
    if escolha == 'A' or escolha == 'a':
        print(20*16 + 10*8)
    else:
        print(20*16 + 5*8)