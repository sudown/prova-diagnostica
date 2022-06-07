#1.000.000.000
Unidade = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
Dezena = ['','dez','vinte', 'trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
Centena = ['cem','cento','duzentos','trezentos','quatrossentos','quinhentos','seissentos','setessentos','oitossentos','novessentos']

def exibe_unidade(N):
    global Unidade
    print(Unidade[N],' ', end = '')

def exibe_dezena(N):
    global Dezena
    global Numero
    unidade = len(Numero) -1
    dezena = len(Numero) -2
    if Numero[unidade] == '0': 
        print(Dezena[N],' ', end = '')
    elif Numero[dezena] != '1':
        print(Dezena[N],' ', end = '')
        print('e ', end = '')
        exibe_unidade(int(Numero[unidade]))
    else: 
        if Numero[unidade] == '1':
            print('onze', end = '')
        elif Numero[unidade] == '2':
            print('doze', end = '')
        elif Numero[unidade] == '3':
            print('treze', end = '')
        elif Numero[unidade] == '4':
            print('quatorze', end = '')
        elif Numero[unidade] == '5':
            print('quinze', end = '')
        elif Numero[unidade] == '6':
            print('dezesseis', end = '')
        elif Numero[unidade] == '7':
            print('dezessete', end = '')
        elif Numero[unidade] == '8':
            print('dezoito', end = '')
        else:
            print('dezenove', end = '')

def exibe_centena(N):
    global Centena
    dezena = len(Numero) -2
    
    if N != 0:
        if Numero[dezena] == '0' and Numero[dezena+1] == '0':
            print(Centena[0],'', end = '')
        else:
            print(Centena[N],'', end = '')
        
    else:
        "Nao consigo ler nada"
    
Numero = input('Digite um número inteiro: ')
Tamanho = len(Numero)


if Tamanho == 9:
    CemMilhao = Numero[0]
    DezMilhao = Numero[1]
    UnidadeMilhao = Numero[2]
    CemMilhar = Numero[3]
    DezMilhar = Numero[4]
    Milhar = Numero[5]
    Centenas = Numero[6]
    Dezenas = Numero[7]
    Unidades = Numero[8]
    CemMilhao = int(CemMilhao)
    DezMilhao = int(DezMilhao)
    UnidadeMilhao = int(UnidadeMilhao)
    CemMilhar = int(CemMilhar)
    DezMilhar = int(DezMilhar)
    Milhar = int(Milhar)
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 8:
    DezMilhao = Numero[0]
    UnidadeMilhao = Numero[1]
    CemMilhar = Numero[2]
    DezMilhar = Numero[3]
    Milhar = Numero[4]
    Centenas = Numero[5]
    Dezenas = Numero[6]
    Unidades = Numero[7]
    DezMilhao = int(DezMilhao)
    UnidadeMilhao = int(UnidadeMilhao)
    CemMilhar = int(CemMilhar)
    DezMilhar = int(DezMilhar)
    Milhar = int(Milhar)
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 7:
    UnidadeMilhao = Numero[0]
    CemMilhar = Numero[1]
    DezMilhar = Numero[2]
    Milhar = Numero[3]
    Centenas = Numero[4]
    Dezenas = Numero[5]
    Unidades = Numero[6]
    UnidadeMilhao = int(UnidadeMilhao)
    CemMilhar = int(CemMilhar)
    DezMilhar = int(DezMilhar)
    Milhar = int(Milhar)
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 6:
    CemMilhar = Numero[0]
    DezMilhar = Numero[1]
    Milhar = Numero[2]
    Centenas = Numero[3]
    Dezenas = Numero[4]
    Unidades = Numero[5]
    CemMilhar = int(CemMilhar)
    DezMilhar = int(DezMilhar)
    Milhar = int(Milhar)
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 5:
    DezMilhar = Numero[0]
    Milhar = Numero[1]
    Centenas = Numero[2]
    Dezenas = Numero[3]
    Unidades = Numero[4]
    DezMilhar = int(DezMilhar)
    Milhar = int(Milhar)
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 4:
    Milhar = Numero[0]
    Centenas = Numero[1]
    Dezenas = Numero[2]
    Unidades = Numero[3]
    Milhar = int(Milhar)
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 3:
    Centenas = Numero[0]
    Dezenas = Numero[1]
    Unidades = Numero[2]
    Centenas = int(Centenas)
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
elif Tamanho == 2:
    Dezenas = Numero[0]
    Unidades = Numero[1]
    Dezenas = int(Dezenas)
    Unidades = int(Unidades)
else:
    Unidades = Numero[0]
    Unidades = int(Unidades)



if Tamanho == 1:
    exibe_unidade(Unidades)
elif Tamanho == 2:
    exibe_dezena(Dezenas)
elif Tamanho == 3:# Tamanho 3:
    exibe_centena(Centenas)
    print('', end = '')
    exibe_dezena(Dezenas)
elif Tamanho == 4:
    exibe_unidade(Milhar)
    print("mil ", end="")
    exibe_centena(Centenas)
    exibe_dezena(Dezenas)
elif Tamanho == 5:
    Numero2 = Numero
    Numero = ""
    c = 0
    for i in range(0, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 2:
            #print(Numero)
            break
    
    exibe_dezena(DezMilhar)
    Numero = Numero2
    print("mil ", end="")
    exibe_centena(Centenas)
    exibe_dezena(Dezenas)
elif Tamanho == 6:
    Numero2 = Numero
    Numero = ""
    c = 0
    for i in range(0, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 3:
            #print(Numero)
            break
    exibe_centena(CemMilhar)
    exibe_dezena(DezMilhar)
    print("mil")
    Numero = Numero2
    exibe_centena(Centenas)
    exibe_dezena(Dezenas)
elif Tamanho == 7:
    Numero2 = Numero
    Numero = ""
    c = 0
    for i in range(0, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 1:
            #print(Numero)
            break
    exibe_unidade(UnidadeMilhao)
    if UnidadeMilhao == 1:
        print("milhão")
    else:
        print("milhões")
    Numero = ""
    c = 0
    for i in range(1, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 3:
            #print(Numero)
            break

    exibe_centena(CemMilhar)
    exibe_dezena(DezMilhar)
    print("mil")
    Numero = Numero2
    exibe_centena(Centenas)
    exibe_dezena(Dezenas)
elif Tamanho == 8:
    Numero2 = Numero
    Numero = ""
    c = 0
    for i in range(0, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 2:
            #print(Numero)
            break
    exibe_dezena(DezMilhao)
    print("milhões")
    Numero = ""
    c = 0
    for i in range(2, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 3:
            #print(Numero)
            break
    exibe_centena(CemMilhar)
    exibe_dezena(DezMilhar)
    print("mil")
    Numero = Numero2        
    exibe_centena(Centenas)
    exibe_dezena(Dezenas)
elif Tamanho == 9:
    Numero2 = Numero
    Numero = ""
    c = 0
    for i in range(0, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 3:
            break
    exibe_centena(CemMilhao)
    Numero = ""
    c = 0
    for i in range(1, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 2:
            break
    exibe_dezena(DezMilhao)
    print("milhões")
    Numero = ""
    c = 0
    for i in range(3, len(Numero2) -1):
        c += 1
        Numero += Numero2[i]
        if c == 3:
            break
    exibe_centena(CemMilhar)
    exibe_dezena(DezMilhar)
    print("mil")
    Numero = Numero2        
    exibe_centena(Centenas)
    exibe_dezena(Dezenas)
elif Tamanho == 10:
    print("Um bilhão")
    
else:
    print("Numero não suportado")