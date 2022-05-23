sexo = '1'
media_mulheres = 0
nome_homem_mais_velho = ''
nome_homem_mais_novo = ''
idade_homem_mais_velho = 0
idade_homem_mais_novo = 1000**1000
qnt_mulheres_maiores_de_idade = 0
c = -1

while sexo == '1' or sexo == '2':
    sexo = input('1- para homem 2- para mulher 0- para sair: ')
    if sexo == '2':
        c += 1
        nome_mulher = input('Digite o nome da mulher: ')
        idade_mulher = int(input('Digite a idade da mulher: '))
        if idade_mulher > 17:
            media_mulheres += idade_mulher
            qnt_mulheres_maiores_de_idade += 1
    
    elif sexo == '1':
        nome_homem = input('Digite o nome do homem: ')
        idade_homem = int(input('Digite a idade do homem: '))

        if idade_homem > idade_homem_mais_velho:
            idade_homem_mais_velho = idade_homem
            nome_homem_mais_velho = nome_homem
        
        elif idade_homem < idade_homem_mais_novo:
            nome_homem_mais_novo = nome_homem
            idade_homem_mais_novo = idade_homem
if c < 0:
    print('XAU')
else:        
    print('Media das mulheres maiores de idade =', media_mulheres/qnt_mulheres_maiores_de_idade)
    print('Nome e idade do homem mais velho =',nome_homem_mais_velho,'',idade_homem_mais_velho)
    print('Nome e idade do homem mais novo =',nome_homem_mais_novo,'',idade_homem_mais_novo)