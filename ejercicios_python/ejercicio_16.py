from rich.console import Console
console = Console()
from util import es_palabra
def capitalizar(cadena):
    return cadena.title()

def ingresar_cadena():
    while True:
        oracion=es_palabra(console.input("[bold blue]Digite una cadena de mminimo 5 palabras\n"))
        if es_palabra(oracion):
            if len(oracion.split()) >= 5:
                console.print(f"[bold green]La cadena capitalizada es {capitalizar(oracion)}[bold green]")
                return
            else:
                console.print("[bold red]La cadena ingresada tiene menos de 5 palabras[bold red]")
                continue

        else:
            console.print(f"[bold red]Cadena vacía[bold red]")
            break
if __name__=="__main__":
    ingresar_cadena()