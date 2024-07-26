import math

p = input('Ingrese el Precio de suscripcion:')
un = input('Ingrese el numero de usuarios normales: ')
up = input('Ingrese el numero de usuarios premium:')
g = input('Ingrese el gasto total:')

p_n = float(p)
p_p = float (p) + (float(p) /100) * 50

pun = float(p_n) * float(un)
pup = float(p_p) * float(up) 

Util = float(pun) + float(pup) - float(g)

print(f'Las utilidades corresponden a {Util:.2f}')
