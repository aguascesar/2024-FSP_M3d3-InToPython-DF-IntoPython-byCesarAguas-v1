import math

p = input('Ingrese el Precio de suscripcion, ej: numeros enteros:')
u = input('Ingrese el numero de usuarios normales, ej: numeros enteros: ')
g = input('Ingrese el gasto total, ej: numeros enteros:')
ua = input('Ingrese las utlidades del año anterior, ej: numeros enteros:')

Up = float(p) * float(u) - float(g)
Util = float(Up) / float(ua)

print(f'Las utilidades actuales corresponden a {Up:.2f}\n')
print(f'La razon entre utilidades actuales y anteriores es: {Util:.2f}\n')
