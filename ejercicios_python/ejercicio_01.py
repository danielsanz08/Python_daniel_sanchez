from util import es_numero_entero
from rich.console import Console
console = Console()
def hallar_cociente():
    console.print("[bold green]Hallar cociente[bold green]")
    
    while True:
        # Solicitar las entradas
        numero_1 = es_numero_entero(console.input("[bold blue]Digite el primer número:[bold blue]\n "))
        numero_2 = es_numero_entero(console.input("[bold blue]Digite el segundo número:[bold blue]\n "))
        
        # Verificar si el segundo número es cero
        if numero_2 == 0:
            console.print("[bold red]ERROR: Es una indeterminación[bold red]")
            continue
        else:
            resultado = round(numero_1 / numero_2, 2)
            console.print(f"[bold green]El resultado es: {resultado}[bold green]:smiley:")
            break

if __name__ == "__main__":
    hallar_cociente()



