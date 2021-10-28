#!/usr/bin/python3

class OptionInvalidError(Exception):
    def __init__(self, option):
        self.option=option

    def __str__(self): # definir em forma de texto o objeto
        if self.option is not None:
            return f'InvalidOptionError: Option {self.option} does not exist'
        return F'InvalidOptionError: Option is absent'

# raise invoca o erro no ato, serve para testar as exeções

def raise_for_invalid_option(option, dic):
    if option not in dic.keys():
        raise OptionInvalidError

dic = {'1': '1', '2': '2'}

try:
    op = input('')
    raise_for_invalid_option(op, dic)

except OptionInvalidError as err:
    print(err)

else:
    print(dic[op])

exit()