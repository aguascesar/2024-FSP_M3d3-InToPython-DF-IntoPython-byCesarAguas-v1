import math
Ve = float
r = input('Ingrese el radio r en Kilometros:')
g = input('Ingrese la constante g: ')

Ve = math.sqrt(2 * (float(g) * (float(r) * 1000)))
print(f'La velocidad de Escape es {Ve:.1f} m/s')


