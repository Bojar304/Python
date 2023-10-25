import random
from time import sleep

num = random.randint(0, 10)
print('Sou seu computador...')
sleep(0.8)
print('Acabei de pensar em um numero entre 0 e 10')
sleep(1.5)
print('Sera que consegue adivinhar qual foi?')
sleep(1.5)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    palpites += 1 #recebe mais 1
    if jogador == num:
        acertou = True
    else:
        if num > jogador:
            print('mais!')
        elif num < jogador:
            print('Menos!')
print('PROCESSANDO...')
sleep(2)
print('Depois de \033[31m{}\033[m tentativas você Acertou, \033[32mPARABÉNS!\033[m'.format(palpites))


