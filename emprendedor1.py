import math
Up = float
p = input('Ingrese el Precio de suscripcion:')
u = input('Ingrese el numero de usuarios: ')
g = input('Ingrese el gasto total:')

Up = float(p) * float(u) - float(g)
print(f'Las utilidades corresponden a {Up:.2f}')

