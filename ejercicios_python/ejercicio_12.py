from rich.console import Console
console = Console()
from util import es_numero_entero
"""
Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el número de
cifras sea par y verificar si el número es capicúa o no.
"""
def numero_capicua(numero):
        """
    Función que verifica si un número es capicúa.

    Args:
    - numero (int): Número entero que se desea verificar.

    Returns:
    - bool: True si el número es capicúa, False de lo contrario.
    """
        numero_str=str(numero)
        if len(numero_str)%2==0:
            if numero_str==numero_str[::-1]:
                console.print(f"[bold green]El número {numero_str} es capicúa[bold green]")
                return True
            else:
               console.print("[bold yellow]El numero no es capicúa[bold yellow]")
            return False
        else:
            console.print(f"[bold yellow]El numero no es de cifras pares[bold yellow]")
            return False
            
def pedir_numeros():
    while True:
        numero=es_numero_entero(console.input("[bold blue]Digite un numero[bold blue]\n"))
        number=int(numero)
        if number>0:
            console.print(f"[bold green]{numero_capicua(numero)}[bold green]")
            break
        else:
            console.print("[bold yellow]Digite numeros positivos unicamente[bold yellow]")
            continue
if __name__=="__main__":
    pedir_numeros()