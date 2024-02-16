# Consigna: ✍️
# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  Para ellos debemos definir una función que reciba parámetros:
# Combinar funciones nativas y funciones definidas,
# condicionales, y bucles.
# Si el usuario ingresa el nro 1, realiza la acción A.
# Si el usuario ingresa el nro 2, realiza la acción B.

def acciones(num, opc):
    if opc == '1':
        print('Los numeros se van a sumar')
        return int(num[0]) + int(num[1])
    elif opc == '2':
        print('Los numeros se van a multiplicar')
        return int(num[0])*int(num[1])

numeros = []
for i in [1,2]:
    numeros.append(input('Ingresa el %i° numero: ' %(i)))

print('Numeros ingresados: %s' %(numeros))

opcion = input('Seleccione una de las siguientes opciones:\n'
               '1 - Sumar los numeros\n'
               '2 - Multiplicar los numeros\n'
               'Ingrese (1/2): ')

if (opcion == '1') or (opcion == '2'):
    print('Opcion %s seleccionada' %opcion)
    resultado = acciones(numeros, opcion)
    print('El resultado es: %i' %int(resultado))
else:
    print('Opcion invalida, intente nuevamente.')
