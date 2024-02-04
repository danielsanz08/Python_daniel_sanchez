from datetime import datetime
from rich.console import Console
console = Console()

def validar_fecha(cadena: str, formato: str = "%Y%m%d") -> bool:
    try:
        fecha = datetime.strptime(cadena, formato)
        anio = fecha.year
        mes = fecha.month
        dia = fecha.day
        return True
    except ValueError as msg_error:
        console.print(f"[bold red]Error: {msg_error}[bold red]")
        return False

def extraer_fecha(fecha: int) -> ():
    str_fecha = str(fecha)
    if len(str_fecha) == 8:
        if validar_fecha(str_fecha):
            return str_fecha[:4], str_fecha[4:6], str_fecha[6:8]
        else:
            console.print(f"[bold yellow]La cadena {str_fecha} no está en el formato aaaammdd...[bold yellow]")
    else:
        console.print(f"[bold red]La cadena {str_fecha} no está en el formato aaaammdd...[bold red]")

def menu_validar_fecha():
    console.print("[bold green]Validación de fecha (aaaammdd)[bold green]")
    numero = console.input("[bold blue]Ingrese una fecha en el formato aaaammdd\n[bold blue]")
    result = extraer_fecha(numero)
    if result:
        console.print(f"[bold green]El número {numero} representa la fecha {result[2]}/{result[1]}/{result[0]} que es válida[bold green]")

if __name__ == "__main__":
    menu_validar_fecha()
