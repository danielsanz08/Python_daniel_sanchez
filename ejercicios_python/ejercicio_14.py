from util import es_letra
from rich.console import Console
console = Console()
"""
Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma.
Una cadena se dice palíndromo si al invertirla es igual a ella misma. 
"""
def es_palindroma(cadena):
    """
    Función que verifica si una cadena es un palíndromo.

    Args:
    - cadena (str): Cadena que se desea verificar.

    Returns:
    - bool: True si la cadena es un palíndromo, False de lo contrario.
    """
    return cadena == cadena[::-1]


def pedir_cadena():
    while True:
        str_cadena = console.input("[bold blue]Digite una cadena: [bold blue]\n")
        if not str_cadena:
            console.print("[bold red]Cadena vacía[bold red]")
            continue

        if es_letra(str_cadena):
            if es_palindroma(str_cadena):
                console.print(f"[bold green]La cadena {str_cadena} es palíndroma[bold green]")
            else:
                console.print(f"[bold yellow]La cadena {str_cadena} no es palíndroma[bold yellow]")
            break
if __name__=="__main__":
    pedir_cadena()