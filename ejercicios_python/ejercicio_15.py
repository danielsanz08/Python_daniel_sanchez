from num2words import num2words
from rich.console import Console
console = Console()
from util import es_numero_entero
def numero_palabra(numero):
    palabra = num2words(numero, lang='es')
    return palabra

def solicitar_numero():
    number = es_numero_entero(console.input("[bold blue]Digite un número: [bold blue]\n")
)
    numero = int(number)
    if 0 <= numero <= 90:
        console.print(f"[bold green]El número {numero} se escribe {numero_palabra(numero)}[bold green]")
    else:
        console.print(f"[bold green]El número {numero} se escribe  {numero_palabra(numero)}[bold green]")
        
   

if __name__ == "__main__":
    solicitar_numero()
