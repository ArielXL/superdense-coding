

def welcome():

    while True:

        option = print_welcome()
        if option >= 1 and option <= 4:
            break
        else:
            print('Por favor, selecciona una opción válida\n')

    return option

def print_welcome():

    print('BIENVENIDO AL PROTOCOLO DE CODIFICACIÓN SUPERDENSA\n')
    print('Escoja la opción deseada:')
    print('1. Protocolo de codificación superdensa')
    print('2. Información de los desarrolladores')
    print('3. Imprimir la información de la aplicación')
    print('4. Salir')
    option = int(input())

    return option