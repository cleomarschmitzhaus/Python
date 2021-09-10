#!/usr/bin/python3

import os

os.system('ls -la')

# Declarar variavel de ambiente com senha no linux = export PASSWD='1234556'
# import os
senha = os.environ['PASSWD']
print(senha)

os.system('pwd')
print(os.system('pwd'))
# os.system('tree .')


exit()
