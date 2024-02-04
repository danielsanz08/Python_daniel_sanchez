from rich.console import Console
console = Console()
from util import es_numero_entero
"""Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en orden inverso.
Ej: Si el número es 324, se debe mostrar 4, 2, 3. """

def invertir(numero):
    """
    Función que invierte un número.

    Args:
    - numero (int or float): Número entero o de punto flotante que se desea invertir.

    Returns:
    - str: Cadena que representa el número invertido.
    """
    cadena_numero=str(numero)
    numero_invertido=",".join(cadena_numero[::-1])
    return numero_invertido
def pedir_numeros():
    while True:
        numero_a=es_numero_entero(console.input("[bold blue]digite un numero[bold blue]\n"))
        numero_a_invertir=str(numero_a)
        if len(numero_a_invertir)>=2:
           console.print(f"[bold green]numero invertido {invertir(numero_a_invertir)}[bold green]")
           break
        elif len(numero_a_invertir)<2:
           console.print("[bold yellow]Digita un numero mayor o igual a 2 digitos[bold yellow]")
        continue
if __name__=="__main__":
    pedir_numeros()