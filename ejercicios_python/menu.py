from util import informacion,aviso,error,advertencia,es_numero
import ejercicio_01,ejercicio_02,ejercicio_03,ejercicio_04,ejercicio_05
def menu():

    while True:
        print(informacion("Seleccione un ejercicio a ejecutar:"))
        print("")
        print(informacion("1) Cociente de 2 números:"))
        print("")
        print(informacion("2) Número par o impar"))
        print("")
        print(informacion("3) Hallar area del circulo"))
        print("")
        print(informacion("4) Hallar Multiplo"))
        print("")
        print(informacion("5) Mostrar fecha"))
        print("")
        print(informacion("30) Salir:"))
        opcion = es_numero(input(aviso("Digite un número\n")))
        print("")
        
        # Comprueba si la opción seleccionada por el usuario es válida.
        if not opcion:
            print(error("Intentelo nuevamente"))
        elif opcion ==1:
            ejercicio_01.hallar_cociente()
            
        elif opcion == 2:
            ejercicio_02.par_impar()
        
        elif opcion ==3:
            ejercicio_03.area_circulo()
            
        elif opcion ==4:
            ejercicio_04.hallar_multiplo()
            
        elif opcion ==5:
            ejercicio_05.fecha_digitada()
        elif opcion == 30:
                print(advertencia("Programa finalizado..."))
                exit(0)   
        else:
            print(error("   Opción inválida. Intente nuevamente."))
if __name__ == '__main__':
    print(aviso("Bienvenido a los ejercicios python"))
    print("")
    print(aviso("Daniel Molano Sánchez"))
    print("")
    print(aviso("Ficha:2670142"))
    print("")
    menu()