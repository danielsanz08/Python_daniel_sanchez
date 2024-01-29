from util import informacion,aviso,error,advertencia,es_numero
"""
E02: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario.
La salida del algoritmo será informar si el usuario ingresó un valor par o impar. Sabemos que un número par es
aquel que es divisible por 2 o, también, que un número es par si el valor residual que se obtiene al dividirlo
por 2 es cero. Según lo anterior, podremos informar que el número ingresado por el usuario es par si 
al dividirlo por 2 obtenemos un resto igual a cero. De lo contrario, informaremos que el número es impar
."""
def par_impar():
    print(" ")
    print(aviso("Hallar par e impar"))
    while True:
        try:
            print(" ")
            print(aviso("Digite un numero"))
            numero=es_numero(input())
        except ValueError:
            print(error("Error: Ingrese un número válido."))
            continue

        if numero == 0:
            print("Error: El número no puede ser cero.")
            continue
        elif numero % 2 == 0:
            print(informacion(f"El número {numero} es par"))
        else:
            print(advertencia(f"El número {numero} es impar"))
        break

if __name__ == "__main__":
    par_impar()
