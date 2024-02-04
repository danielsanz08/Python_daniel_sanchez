from util import es_numero_entero
from rich.console import Console
console = Console()
"""
E02: En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario.
La salida del algoritmo será informar si el usuario ingresó un valor par o impar. Sabemos que un número par es
aquel que es divisible por 2 o, también, que un número es par si el valor residual que se obtiene al dividirlo
por 2 es cero. Según lo anterior, podremos informar que el número ingresado por el usuario es par si 
al dividirlo por 2 obtenemos un resto igual a cero. De lo contrario, informaremos que el número es impar
."""
def par_impar():
    console.print(" ")
    console.print("[bold green]Hallar par e impar[bold green]")
    while True:
        numero=es_numero_entero(console.input("[bold blue]Digite un numero\n[bold blue]"))
        if numero ==0:
            console.print(f"[bold red]ERROR[bold red]")
            console.print(f"[bold cyan]Digite de nuevo[bold cyan]")
            continue
        elif numero % 2==0:
            console.print(f"[bold green]El número {numero} es par")
            break
        else:
            console.print(f"[bold green]El número {numero} es impar")
            break
if __name__ == "__main__":
    par_impar()
