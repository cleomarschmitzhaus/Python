#!/bin/bash/python3

import time
import datetime

antes = time.process_time()
depois = time.process_time()

diferenca = depois - antes
print(diferenca)

# Validar tempo
t1 = datetime.datetime.now()
time.sleep(10)
t2 = datetime.datetime.now()
t3 = t2 - t1
print(t3)
print(t1)
str(t1)

exit()