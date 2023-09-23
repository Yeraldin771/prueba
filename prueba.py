un codigo ejemplo 

import string
import random

print('Crearás una o varias contraseñas seguras...\n')

# pool de caracteres
pool_chr = string.ascii_letters + 'ñ'+'Ñ'+ string.digits + string.punctuation

# solicitud de ingreso de número de contraseñas
howMany = int(input('¿Cuantas contraseñas desea crear?\n'))
print('\n')

# solicitud de ingreso de tamaño de la contraseña
lenght = int(input('Tamaño de la Contraseña Segura\n'))
print('\n')

for i in range(howMany):
    psswd = ''
    for n in range(lenght):
        psswd += random.choice(pool_chr)
    print(psswd)
print('\n')