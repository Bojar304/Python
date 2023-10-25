from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano_nascimento = int(input('Qual o ano que {}ª pessoa nasceu?: '.format(pess)))
    idade = atual - ano_nascimento
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} maiores de idade e {} pessoas menores!'.format(totmaior, totmenor))
