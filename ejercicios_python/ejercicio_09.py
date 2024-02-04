from util import es_numero_entero
from rich.console import Console
console = Console()
"""
Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe de imprimir
el mes correspondiente en texto. 
"""
def mes(valor: int):
    """
    Función que toma un número entero y devuelve el nombre del mes correspondiente.

    Args:
    - valor (int): Número entero que representa el mes (de 1 a 12).

    Returns:
    - None: La función imprime el nombre del mes si el valor está entre 1 y 12.
    """
    nombres_meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    if 1 <= valor <= 12:
        console.print(f"[bold green]El número {valor} es {nombres_meses[valor - 1]}[bold green]")
    else:
        print(f"[bold yellow]No hay un mes asociado al número {valor}[bold yellow]")

def obtener_numero():
    numero_str=es_numero_entero(console.input("[bold blue]digite un numero del 1 al 12\n[bold blue]"))
    numero=int(numero_str)
    if 1<= numero <=12:
        console.print("[bold green]Número valido[bold green]")
        mes(numero)
    else:
        console.print("[bold red]ERROR[bold red]")
if __name__=="__main__":
    obtener_numero()