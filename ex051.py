pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dt = pt + 10 * r
for c in range(pt, dt, r,):
    print(c, end=' -> ')
print('Acabou')
print(dt)