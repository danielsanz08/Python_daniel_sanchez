from util import es_letra
from rich.console import Console
console = Console()
"""
Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de ocurrencias de
dicho carácter en una cadena de caracteres.
"""
def contar_ocurrencias(cadena, caracter):
        """
    Función que cuenta el número de ocurrencias de un carácter en una cadena.

    Args:
    - cadena (str): Cadena en la que se buscarán las ocurrencias.
    - caracter (str): Carácter cuyas ocurrencias se contarán.

    Returns:
    - int: Número de ocurrencias del carácter en la cadena.
    """
        ocurrencias_contadas = cadena.count(caracter)
        return ocurrencias_contadas

def pedir_cadena():
    while True:
        cadena_str = es_letra(console.input("[bold green]Digite una cadena: [bold green]\n"))
        
        if cadena_str:
            while True:
                letra_str = es_letra(console.input("[bold blue]Digite una letra que quiera contar dentro de la cadena: [bold blue]"))
                
                if letra_str:
                    resultado = contar_ocurrencias(cadena_str, letra_str)
                    console.print(f"[bold green]La cantidad que se repite es: {resultado}[bold green]")
                    return
                else:
                    console.print("[bold red]No has digitado la letra que quieres contar.[bold red]\n")
        else:
            console.print("[bold red]No has digitado la cadena.[bold red]")

if __name__ == "__main__":
    pedir_cadena()
