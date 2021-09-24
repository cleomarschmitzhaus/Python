#!/usr/bin/python3

# como acessar aquivos?

# 1 abertura do arquivo, serve somente como acesso
arquivo = open('arquivo.txt','r')
# arquivo = open('.../caminho_completo/arquivo.txt', 'r') -> caminho e modo de leitura = r

# 2 Consultart o conteudo
# tudo que tem dentro de "arquivo"
# conteudo = arquivo.read()
conteudo = arquivo.readlines() ## Tambem pode transformar tudo em lista com o numero de linhas, toda vez que encontrar o /n
# é transformado tudo em string

# 3 é necessário fechar o arquivo toda a vez
arquivo.close()

# 4 mostra o conteudo
print(conteudo)

exit()

#### modulos de escritas

# modo 'w' ele trunca o arquivo, grava por cima um arquivo vazio
# dai deve abrir o arquivo antes e capturar o conteudo
# altera o conteudo
# grava a modificação
arquivo = open('arquivo.txt')
conteudo = arquivo.readlines()
arquivo.close()
conteudo.append('nova linha de exemplo') # conteudo modificado

## altera esse conteudo
# 1 abertura do arquivo

arquivo = open('arquivo.txt')
arquivo.writelines(conteudo)
arquivo.close()

# forma de abrir o arquivo sem subscrever tudo
arquivo = open('arquivo.txt','a')
arquivo.write('adicionei uma nova linha')
arquivo.close()

# mode x cria arquivo e não substitui o arquivo caso exista
arquivo = open('cria_arquivo.txt','x')
arquivo.write('nova linha\n')
arquivo.close()
