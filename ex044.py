import time
print('{:=^40}'.format('LOJAS BOJAR'))
time.sleep(1)
preço = float(input('Preço da compra: '))
print('!= FORMAS DE PAGAMENTO =!')
time.sleep(1)
print('''[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x no cartão ou mais no cartão''')
opção = int(input('Qual sua opção??: '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcelas = total / 2
    print('Sua compra sera parcelada em 2x de {} vezes'.format(parcelas))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?: '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de {:.2f} COM JUROS'.format(totparc, parcela))

print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, total))
