from rich.console import Console
from rich.table import Table
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
 "[bold blue]4) Hallar Multiplo[bold blue]",
    
)
table.add_row(
 "[bold blue]2) Número par o impar[bold blue]",
    
)
table.add_row(
    "[bold blue]5) Mostrar fecha[bold blue]"

)
table.add_row(
    "[bold yellow]30) Salir:[bold yellow]"
)
console.print(table)
opcion=console.input("[bold green]Digite un numero[bold green]\n")
opcion_int=int(opcion)
print("")
        
# Comprueba si la opción seleccionada por el usuario es válida.
if not opcion_int:
    console.print("[bold blue]Intentelo nuevamente[bold blue]")
elif opcion_int ==1:
     console.print("hola")
            
elif opcion_int == 2:
    console.print("hola")    
elif opcion_int ==3:
    console.print("hola")
            
elif opcion_int ==4:
    console.print("hola")
            
elif opcion_int ==5:
    console.print("hola")
elif opcion_int == 30:
    console.print("[bold yellow]Programa finalizado...[bold yellow]")
    exit(0)   
else:
    console.print("[magenta blue]Opción inválida. Intente nuevamente.[bold magenta]")
