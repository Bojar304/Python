from time import sleep

sm = 1
multiplicar = 2
maior = 3
novosnums = 4

pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))

op = 0

while op != 5:
    print('=-='*10)
    print(' [ 1 ] somar\n [ 2 ] multiplicar\n [ 3 ] maior\n [ 4 ] novos numeros\n [ 5 ] Sair do programa ')
    op = int(input('>>>>> Qual é a sua opção?: '))
    if op == sm:
        sm = (pv + sv)
        print(' A soma entre {} + {} é {}'.format(pv,sv, sm))
    elif op == multiplicar:
        multiplicar = (pv * sv)
        print('O resultado de {} X {} é {}'.format(pv, sv, multiplicar))
    elif op == maior:
        if pv > sv:
            maior = pv
        else:
            maior = sv
        print('o maior valor é {}'.format(maior))
    elif op == novosnums:
        print('informe os numeros novamente')
        pv = int(input('Digite o primeiro valor: '))
        sv = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção invalida, tente novamente')
    sleep(1)
print('Fim do programa!')
