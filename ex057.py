sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] # o 0 e para o programa pegar apenas a primeira letra
while sexo not in 'MmFf': #while = enquanto = enquanto o sexo não for MmFf
    sexo = str(input('Dados inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
