from util import es_numero_entero
from rich.console import Console
console = Console()
#Función que convierte una cantidad de segundos a horas.
def obtener_horas(segundos):
    horas = round(segundos / 3600, 3)
    return horas
#Función que convierte una cantidad de segundos a minutos.
def obtener_minutos(segundos):
    minutos = round(segundos / 60)
    return minutos

def pedir_valor():
        console.print("[bold yellow]Convertir sgs a mts y hrs[bold yellow]")
        segundos = es_numero_entero(console.input("[bold blue]Digite el tiempo que invierte en hacer un examen en segundos:[bold blue] \n"))
        
        if segundos > 0:
            horas = obtener_horas(segundos)
            minutos = obtener_minutos(segundos)
            console.print(f"[bold green]Invierte {horas} horas en hacer un examen[bold green]")
            console.print(f"[bold blue]Invierte {minutos} minutos en hacer un examen[bold blue]")
            console.print(f"[bold yellow]Invierte {segundos} segundos en hacer un examen[bold yellow]")
        else:
            console.print("[bold red]Ingresa un valor positivo para los segundos.[bold red]")


if __name__ == "__main__":
    pedir_valor()
