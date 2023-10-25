from time import sleep
print('='*26)
print('Seguência de Fibonacci')
print('='*26)

#print('-'*40)
n = int(input('Quantos termos você quer mostrar? '))
#print('-'*40)

ultimo = 0
penultimo = 1

print('~~'*20)
count = 3
print('{} -> '.format(0),end='')

while count <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    sleep(1)
    print('{} -> '.format(termo),end='')
print('Fim')
print('~~'*20)
