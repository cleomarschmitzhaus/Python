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

#### Arquivos -> iniciar em modulos de escritas