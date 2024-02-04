from util import es_numero_entero
from rich.console import Console
console = Console()
"""En este problema tenemos un único dato de entrada: un valor numérico entero que deberá ingresar el usuario.
La salida del algoritmo será informar si el numero ingresado por el usuario es múltiplo de 2 y 3. Sabemos
que un número es múltiplo de otro cuando al dividir estos dos números el residuo sea 0. Si el usuario ingresó
un valor negativo o cero tendremos que emitir un mensaje informando las causas por las cuales no se podrá 
efectuar la operación. 
"""
def hallar_multiplo():
    console.print("[bold green]Verificar si es múltiplo de 2 y 3[bold green]")
    print(" ")
    while True:
        numero=es_numero_entero(console.input("[bold blue]Digite un numero[bold blue]\n"))
        if numero <=0:
            print("[bold red]No permitido[bold red]")
            print("[bold yellow]Digita un numero mayor a 0 por favor[bold yellow]\n")
            
        elif numero % 2== 0 and numero % 3==0:
            console.print(f"[bold green]El número {numero} es múltiplo de 2 y de 3[bold green]:smiley:")
            break
        else:
            console.print(f"[bold yellow]El número {numero} no es múltiplo de 2 y de 3[bold yellow]")
            break
if __name__=="__main__":
    hallar_multiplo()