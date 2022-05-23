kwh = abs(int(input('Digite a quantidade de quilowatt/hora: ')))

print('')
bandeira = input('1- para Verde 2- Amarela -3 Vermelha1 4- Vermelha2: ')
if bandeira == '1':
    print('Sua conta de luz deu:', kwh*10,'R$')
elif bandeira == '2' :
    print('Sua conta de luz deu:', (kwh / 100) * 1 + (kwh*10),'R$')
elif bandeira == '3' :
    print('Sua conta de luz deu:', (kwh / 100) * 3 + (kwh*10),'R$')
elif bandeira == '4' :
    print('Sua conta de luz deu:', (kwh / 100) * 5 + (kwh*10),'R$')