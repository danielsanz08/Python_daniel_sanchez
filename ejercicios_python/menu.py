from rich.console import Console
from rich.table import Table
from util import es_numero_entero
import ejercicio_01,ejercicio_02,ejercicio_03,ejercicio_04,ejercicio_05
import ejercicio_06,ejercicio_07,ejercicio_08,ejercicio_09,ejercicio_10
import ejercicio_11,ejercicio_12,ejercicio_13,ejercicio_14,ejercicio_15,ejercicio_16
console = Console()
if __name__ == '__main__':
    console.print("[bold green]Bienvenido a los ejercicios python[bold green]")
    console.print("")
    console.print("[bold green]Daniel Molano Sánchez[bold green]")
    console.print("")
    console.print("[bold green]Ficha:2670142[bold green]")
    console.print("")
    
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Menu", style="bright", width=45)

table.add_row(
    "[bold green]--Menú--[bold green]"
)
table.add_row(
    "[bold red]Seleccione un ejercicio a ejecutar:[/bold red]",
)
table.add_row(
    "[bold blue]1) Cociente de 2 números:[/bold blue]",
)
table.add_row(
 "[bold blue]2) Número par o impar[bold blue]",
    
)
table.add_row(
 "[bold blue]3) Hallar area del circulo[bold blue]",
    
)
table.add_row(
 "[bold blue]4) Hallar Multiplo de 2 y 3[bold blue]",
    
)
table.add_row(
    "[bold blue]5) Mostrar fecha[bold blue]"

)
table.add_row(
    "[bold blue]6) Hallar el tamaño de 3 numeros[bold blue]"

)
table.add_row(
    "[bold blue]7) Hallar hipotenusa[bold blue]"

)
table.add_row(
    "[bold blue]8) Digitar fecha[bold yellow]"
)
table.add_row(
    "[bold blue]9) Mostrar mes[bold blue]"
)
table.add_row(
    "[bold blue]10) Convertir de sg a mts y a hrs[bold blue]"
)
table.add_row(
    "[bold blue]11) Mostrar numeros inversamente[bold blue]"
)
table.add_row(
    "[bold blue]12) Contar la cantidad de 1 letra de una cadena[bold blue]"
)
table.add_row(
    "[bold blue]13) Contar la cantidad de 1 letra de una cadena[bold blue]"
)
table.add_row(
    "[bold blue]14) Verificar si es palíndroma[bold blue]"
)
table.add_row(
    "[bold blue]15) De número a palabra[bold blue]"
)
table.add_row(
    "[bold blue]16) Capitalizar cadena[bold blue]"
)
table.add_row(
    "[bold yellow]30) Salir:[bold yellow]"
)
console.print(table)
while True:
    opcion=es_numero_entero(console.input("[bold green]Digite un número\n[bold green]"))
    opcion_int=int(opcion)
    print("")
        
    # Comprueba si la opción seleccionada por el usuario es válida.
    if not opcion_int:
        console.print("[bold blue]Intentelo nuevamente[bold blue]")
    elif opcion_int ==1:
        ejercicio_01.hallar_cociente()
    elif opcion_int == 2:
        ejercicio_02.par_impar()
    elif opcion_int ==3:
        ejercicio_03.area_circulo()
            
    elif opcion_int ==4:
        ejercicio_04.hallar_multiplo()
            
    elif opcion_int ==5:
        ejercicio_05.menu_validar_fecha()
    elif opcion_int ==6:
        ejercicio_06.menu_tamaño()
    elif opcion_int ==7:
        ejercicio_07.pedir_catetos()
    elif opcion_int ==8:
        ejercicio_08.menu_validar_fecha()
    elif opcion_int==9:
         ejercicio_09.obtener_numero()
    elif opcion_int==10:
        ejercicio_10.pedir_valor()
    elif opcion_int==11:
        ejercicio_11.pedir_numeros()
    elif opcion_int==12:
        ejercicio_12.pedir_numeros()
    elif opcion_int==13:
        ejercicio_13.pedir_cadena()
    elif opcion_int==14:
        ejercicio_14.pedir_cadena()
    elif opcion_int==15:
        ejercicio_15()
    elif opcion_int==16:
        ejercicio_16()
    elif opcion_int == 30:
        console.print("[bold yellow]Programa finalizado...[bold yellow]")
    exit(0)   


    
