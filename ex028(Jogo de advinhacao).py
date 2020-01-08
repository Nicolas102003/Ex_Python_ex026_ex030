import random
from time import sleep
num = random.randint(0, 5)
print('vou pensar em um numero de 0 a5 tente adivinhar ')
adv = int(input('Em que número eu estou pensando ??'))
print('Processando...')
sleep(1.5)
if adv == num:
    print('Parabens!!! você me venceu')
else:
    print('Errou o número era {} e não {}'.format(num,adv))
print('---FIM---')
print(num)
