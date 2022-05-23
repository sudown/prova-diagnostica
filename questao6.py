
aposta = ['' for i in range(0,6)]
c = 0

while c < 6:
    dezena = abs(int(input('Digite uma: ')))
    if dezena > 0 and dezena < 61 and dezena != aposta[0] and dezena != aposta[1] and dezena != aposta[2] and dezena != aposta[3] and dezena != aposta[4] and dezena != aposta[5]:
        if dezena < 10:
            dezena = str(dezena)
            aposta[c] = '0'+dezena
        else:
            aposta[c] = dezena
    
    else:
        print('Numero invalido')
        c -= 1
    c += 1

for i in range(0,len(aposta)):
    for j in range(0,len(aposta) -1):
        if aposta[i] < aposta[j]:
            swap = aposta[i]
            aposta[i] = aposta[j]
            aposta[j] = swap

print(aposta)