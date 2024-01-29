from util import aviso,informacion,error,es_numero
"""
E01: En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a través 
del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora bien, existe
la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En este caso, no podremos 
mostrar el cociente ya que la división por cero es una indeterminación, así que tendremos que emitir un mensaje
informando las causas por las cuales no se podrá efectuar la operación. 

"""
def hallar_cociente():
    print(informacion("Hallar cociente"))
    while True:
        numero_1 = es_numero(input(aviso("Digite el primer número:\n ")))
        if numero_1 == 0:
            print(error("ERROR: El primer número no puede ser cero."))
            continue  # Vuelve al inicio del bucle para solicitar la entrada nuevamente
          
        numero_2 = es_numero(input(aviso("Digite el segundo número: \n")))
        if numero_2 == 0:
            print(error(("ERROR: No se puede realizar porque es una indeterminacion.")))
            continue  # Vuelve al inicio del bucle para solicitar la entrada nuevamente

        # Si ambos números son válidos, realiza la división y muestra el resultado
        resultado = numero_1 / numero_2
        
        break  # Sale del bucle cuando los números son válidos
    print(informacion(f"El resultado es: {resultado}"))
    
    
if __name__ =="__main__":
    hallar_cociente()
    