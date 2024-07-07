def calc():
    soma=0
    for cont in range(n2,n3):
            soma=soma+cont
    return soma
n1=int(input('Lance um número entre 1 e 24:'))
import random
n=random.randint(1,24)
print(
'''________________________________________
|Lançando dados para o tabuleiro......''')
import time
time.sleep(1)
import random
n2=random.randint(1,12)
import random
n3=random.randint(1,12)
resul=calc()
print(
'''_____________________________
|Carregando resultados......''')
time.sleep(1)
print(
'''_____________________________
|Verificando resultados......''')
time.sleep(1)
if resul==n:
    print(
        '''__________________________________
Lucrou com 100€ da sua aposta''')
else:
    print('''______________________________
Perdeu 100€ da sua aposta''')