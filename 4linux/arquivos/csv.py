#!/usr/bin/python3

#with open('cadastro.csv', 'r') as arquivo:
    #cadastro = arquivo.readlines()

#print(cadastro)

# para manipular a lista
# cadastro com o readlines é uma lista
# o primeiro elemento da lista é o cabeçalho -> cpf (0), nome (1), idade (2), sexo (3), uf (4)
# atentar a estrutura do arquivo com quebras de linha

#filtro_uf = 'RJ'

#for registro in cadastro:
    #if registro.split(',')[4] == filtro_uf+'\n':
        #print(registro)

# for registro in cadastro:
    # if filtro_uf in registro.split(',')[4]:
        # print(registro)
        # print('CPF', registro.split(',')[0])
        # print('Nome', registro.split(',')[1])


#exit()

### adicionar um nomo registro

# capturar os dados via teclado

cpf = input('CPF: ')
nome = input('Nome: ')
idade = input('Idade: ')
sexo = input('Sexo: ')
uf = input('UF: ')

registro = f'{cpf},{nome},{idade},{sexo},{uf}\n'

with open('planilha.csv','a') as arquivo:
    arquivo.writelines(registro)

# formato do registro: '00000000000',Cleomar Schmitzhaus,29,F,MG\n'

exit()

### Para fazer alteração de cadastro

cpf = '11111111111'

with open('planilha,csv','r') as arquivo:
    cadastro = arquivo.readlines()

for indice in range(len(cadastro)):
    if cadastro[indice].split(',')[0] == cpf:
        print(cadastro[indice])
        # alteração de valores
        
        # para deletar com del e deve usar o break
        # del cadsatro[indice]
        # break

        # Essa parte de baixo não é necessária quando feito o del
        cpf = input('CPF: ')
        nome = input('Nome: ')
        idade = input('Idade: ')
        sexo = input('Sexo: ')
        uf = input('UF: ')

        cadastro[indice] = f'{cpf},{nome},{idade},{sexo},{uf},\n'

with open('planilha.csv','w') as arquivo:
    arquivo.writelines(cadastro)

exit()

# Deletar dados

