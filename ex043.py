from time import sleep
print('=-'*12)
print('CALCULADORA DE IMC!')
print('=-'*12)
sleep(1)
altura = float(input('Digite sua altura (KG): '))
peso = float(input('Digite seu peso (M): '))
imc = peso/altura
if imc <= 18.5:
    print('Seu imc é {:.2f}, significa que esta abaixo do peso'.format(imc))
elif 18.5 < imc < 25:
    print('Seu imc é {:.2f}, voçe esta no peso ideal'.format(imc))
elif 25 < imc < 30:
    print('Seu imc é {:.2f}, sobre esta com sobre peso'.format(imc))
elif 30 < imc < 40:
    print('Seu imc é {:.2f}, Voce esta com SOBREPESO!, Cuidisse o mais breve!'.format(imc))
else:
    print('Seu imc é {:.2f}, Tu ta com OBESIDADE MORMIDA, vá a um medico urgentemente!!!'.format(imc))
print('seu imc é {:.2f}'.format(imc))
