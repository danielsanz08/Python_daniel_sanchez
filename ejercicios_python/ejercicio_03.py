from util import es_float
from rich.console import Console
console = Console()
"""
E03: En este problema debemos de definir una constante con el valor de PI como 3.1416 y 
tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser
entero o flotante que indicara el radio de un círculo. La salida del algoritmo será el 
área del círculo teniendo en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo
o cero tendremos que emitir un mensaje informando las causas por las cuales no se podrá
efectuar la operación. 
"""
def area_circulo():
    pi = 3.1416
    while True:
        console.print("[bold green] --Hallar area del circulo--")
        radio = es_float(console.input("[bold blue]Digite el radio de un círculo:[bold blue]\n"))
        if radio <= 0:
            console.print("[bold red]ERROR: El radio debe ser un número positivo.[bold red]")
            print("[bold yellow]No se puede hallar el área del círculo. Intenta de nuevo.[bold yellow]")
            continue
        else:
            area = pi * radio**2
            area_round=round(area,3)
            console.print(f"[bold green]El área del círculo es: {area_round}[bold green]:smiley:")
            break

if __name__ == "__main__":
    area_circulo()
