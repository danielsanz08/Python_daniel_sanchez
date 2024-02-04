from util import es_numero_entero
from rich.console import Console
console = Console()
""""
Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el menor. 
Considerar que los tres valores serán diferentes. 
"""
def son_numeros_diferentes(numero_1,numero_2,numero_3):
    return numero_1 !=numero_2 and numero_2 !=numero_3 and numero_3 !=numero_1

        
    
def obtener_tamaño(numero_1,numero_2,numero_3):
    """
    Método que toma tres números como argumentos y devuelve una tupla con el mayor, el mediano y el menor.

    Args:
    - numero_1 (float): Primer número de la secuencia.
    - numero_2 (float): Segundo número de la secuencia.
    - numero_3 (float): Tercer número de la secuencia.

    Return:
    - tuple: Una tupla con el mayor, mediano y menor de los tres números.
    """
    mayor = max(numero_1, numero_2, numero_3)
    menor = min(numero_1, numero_2, numero_3)
    mediano = numero_1 + numero_2 + numero_3 - mayor - menor
    return mayor, mediano, menor

def menu_tamaño():
    console.print("[bold yellow]Hallar el tamaño de 3 números[bold yellow]")
    #Función que solicita al usuario que ingrese tres números y luego imprime el mayor, el mediano y el menor.
    while True:
        numero_1 =es_numero_entero(console.input("[bold blue]1) Digite un numero\n[bold blue]"))
        numero_2 =es_numero_entero(console.input("[bold blue]2) Digite un numero\n[bold blue]"))
        numero_3 =es_numero_entero(console.input("[bold blue]3) Digite un numero\n[bold blue]"))
    
        if son_numeros_diferentes(numero_1, numero_2, numero_3):
            mayor,mediano,menor = obtener_tamaño(numero_1, numero_2, numero_3)
            console.print(f"[bold green]El numero mayor es: {mayor}[bold green]\n[bold yellow]El numero mediano es:[bold yellow] {mediano}\n[bold red]El numero menor es [bold red]{menor}")
            return
        else:
            console.print("[bold yellow]Digite numeros diferentes[bold yellow]")
            continue
   
if __name__ =="__main__":
    menu_tamaño()