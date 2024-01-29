from util import aviso,es_numero,error,informacion
"""
En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el siguiente formato:
aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2 dígitos representan el mes
y los 2 dígitos restantes representan el día. Se pide informar por separado el día, el mes y el año de la
fecha ingresada. Para su solución se debe de hacer uso de divisiones, operador modulo y conversión de double
a entero. 
"""

def obtener_fecha(fecha):
    fecha_int = int(fecha)
    # Obtener año, mes y día por separado
    ano = fecha_int // 10000
    mes = (fecha_int // 100) % 100
    dia = fecha_int % 100
    return ano, mes, dia

while True:
    print(aviso("Digita una fecha con el siguiente formato: AAAAMMDD\n"))
    fecha_digitada=es_numero(input())
    
    

    # Verificar si la longitud de la entrada es correcta
    if len(fecha_digitada) != 8:
        print(error("La fecha debe tener exactamente 8 dígitos."))
        continue

    # Obtener año, mes y día usando la función obtener_fecha
    ano, mes, dia = obtener_fecha(fecha_digitada)

    print(informacion("\nLa fecha digitada es:"))
    print(informacion("Año:", ano))
    print(informacion(("Mes:", mes)))
    print(informacion("Día:", dia))

    # Salir del bucle después de procesar la fecha
    break
