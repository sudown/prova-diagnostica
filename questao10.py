peso_caminhao = abs(float(input('Digite o peso do caminhão: ')))
peso_caminhao_com_carga = abs(float(input('Digite o peso do caminhão com carga: ')))
peso_carga = peso_caminhao_com_carga - peso_caminhao

if peso_carga > peso_caminhao*0.20:
    print('Pague 20 R$')

elif (peso_carga > peso_caminhao*0.10) and (peso_carga <= peso_caminhao*0.20):
    print('Pague 10 R$')

else:
    print('Pode passar sem pagar nada meu consagrado')