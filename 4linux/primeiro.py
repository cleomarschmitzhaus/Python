#Anotações
def hellow(nome: str) -> str:
    return nome

#Inteiros
num = 1
num2 = 10
num3 = 10.5/3.7 #float

#string
texto = 'Cleomar Schmitzhaus\' Atropina'

outro_texto = "Cleomar' Schmitzhaus"

mais_um_teste = '''
SELECT * FROM users
WHERE id = 1
''' 

if num3 > 100:
    print("estou dentro do if")
print("estou fora do if")


# não precisa elseif ou endif
if num3 > 100:
    print("estou dentro do if")
else:
    print("estou fora do if")
elif num2 < 5: # else if -> para validar intervalos
    print("asdjahsjadhsjdash")

"""
Comentário de multilinha, ou o #
"""

#tipos de dados


#strings

# calcular a média de um aluno, foram 3 provas
## saber as notas do aluno
### Informar a primeira nota
nota1 = float(input("Digite a primeira nota"))
### informar a segunda nota
nota2 = float(input("Digite a segunda nota"))
### informar a terceira nota
nota3 = float(input("Digite a terceira nota"))
### Calcular a média
media =  (nota1 + nota2 + nota3)/3
### apresentar o resultado
print("media final é: ", media)


tupla = (1,2,3,4) #imutavel
tupla[2] #apresenta o dado 3
lista = [1,2,3,4,5] #pode modificar mais coisas

for elemento in lista: #elemento - variavel de escopo
    print(elemento)
#for = para
#in = desse/em

controle = 0

while controle <len(tupla):
        print(tupla[controle])

# necessario atualizar a variavel controle

# for é sempre mais amigavel

# in tupla = para cada elemnto da tupla

dicionario = {
    #trabalha com chaves "{}"
    'nome':"Linus Torvalds",
    'email': "pinguin@pinguin.com"
    #key    # value
}

print(dic['email']) # pinhuim@pinguim.com

exit()

# define função com def

#def nome_da_funcao():
    # trecho do codigo

