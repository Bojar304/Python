from random import randint
from time import sleep
print('=-'*20)
print('{:=^40}'.format('GAME PEDRA PAPEL E TESOURA'))
print('=-'*20)

itens = ('pedra', 'papel' , 'tesousa')
computador = randint(0, 2)

print('''Suas opções:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Qual a sua jogada?: '))
sleep(1)
print('JO')
sleep(1.3)
print('KEN')
sleep(1.3)
print('PO!!')
sleep(1)

print('-='* 14)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='* 14)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVALIDA!!!')

elif computador == 1: # computadpr jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('JOGADA INVALIDA!!!')

elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVALIDA!!!')
