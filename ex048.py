print('=-='*20)
print('{:-^60}'.format('NUMEROS IMPARES MULTIPLOS DE 3'))
print('=-='*20)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        cont += 1
        soma += c
print('a soma de todos os {} valores é {}'.format(cont, soma), end=' ')


#if (n1%2) == 0: #%2 o resto da divisao por 2
    #print('o numero {} é \033[;0;34mPAR'.format(n1))
#else:
    #print('O numero {} é \033[31mÍMPAR'.format(n1))