from datetime import date
print('-=-'* 20)
print('--------------CONFEDERAÇÃO NACIONAL DE NATAÇÃO--------------')
print('-=-'*20)
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é \033[31mMirim\033[m')
elif idade <= 14:
    print('Sua categoria é \033[32mInfantil\033[m')
elif idade <= 19:
    print('Sua categoria é \033[33mJunior\033[m')
elif idade <= 20:
    print('Sua categoria é \033[34mSênior\033[m')
else:
    print('Sua categoria e \033[35mMaster\033[m')


