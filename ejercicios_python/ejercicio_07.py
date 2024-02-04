from util import es_float
from rich.console import Console
console = Console()
def validar_cateto(cateto_1, cateto_2):
    """
    Función que valida dos catetos y calcula la hipotenusa si ambos son números válidos.

    Args:
    - cateto_1 (float): Primer cateto a validar.
    - cateto_2 (float): Segundo cateto a validar.

    Returns:
    - None: La función imprime la hipotenusa si ambos catetos son válidos.
    - None: Imprime un mensaje de error si al menos uno de los catetos no es un número válido.
    """
    if cateto_1 is not None and cateto_2 is not None:
        hipotenusa = round((cateto_1**2 + cateto_2**2)**0.5, 3)

        console.print(f"[bold green]La hipotenusa es de: {hipotenusa}[bold green]")
    else:
        console.print("[bold red]ERROR[bold red]")
def pedir_catetos():
    cateto_1 = es_float(console.input("[bold blue]Digite cateto 1: [bold blue]\n"))
    cateto_2 = es_float(console.input("[bold blue]Digite cateto 2: [bold blue]\n"))
    if cateto_1 and cateto_2:
        validar_cateto(cateto_1,cateto_2)
    

        
if __name__ == "__main__":
    pedir_catetos()
