#!/usr/bin/python3

# para evitar conflitos ou para não poluir o ambiente
# "python3-venv" - apt install python3-venv
# "python3 -m venv "- para verificar se esta instalado
# "python3 -m venv meu_ambiente" - para criar o ambiente
# para executar o ambente, dentro de meu_ambeinte/bin

# bin
# include
# lib
# lib64 -> lib
# pyvenv.cfg
# share

# /home/developer/python/4linux/modulos/meu_ambiente/bin#
# dentro de bin -> "source activate"
# nesse ambiente virtual não tem nada instalado
# não é possivel importar de fora do ambente
# para instalar pacotes:
# "pip3 install pymongo" - para instalar dentro do ambente
# para sair do ambente virtualizado: deactivate
# "pip freeze > requirements.txt" - Para salvar as dependencias do meu projeto
# "pip install -r requirements.txt" - para instalar as dependencias apartir de um arquivo "requirements.txt"