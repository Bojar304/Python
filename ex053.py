
frase = str(input('digite uma frase: ')).strip().lower()
palavras = frase.split()
tudo_junto = ''.join(palavras)
inverso =''
#inverso = junto[::-1] outra maneira de fazer sem o for
for letra in range(len(tudo_junto)-1, -1, -1):
    inverso = inverso + tudo_junto[letra]
if inverso == tudo_junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo')
