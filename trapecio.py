#programa que calcula el area de un trapecio 
#allan mendez 
# trapecio.py
def calcular_area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio usando la fórmula A = (B + b) * h / 2
    
    Parámetros:
    base_mayor (float): Base mayor del trapecio (B)
    base_menor (float): Base menor del trapecio (b)
    altura (float): Altura del trapecio (h)
    
    Retorno:
    float: Área del trapecio
    """
    if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
        raise ValueError("Todas las dimensiones deben ser positivas")
    
    area = (base_mayor + base_menor) * altura / 2
    return area

# Si se ejecuta este archivo directamente, solicitar entrada del usuario
if __name__ == "__main__":
    try:
        print("Calculadora de Área de Trapecio")
        print("-------------------------------")
        
        # Solicitar datos al usuario
        base_mayor = float(input("Ingrese la base mayor (B): "))
        base_menor = float(input("Ingrese la base menor (b): "))
        altura = float(input("Ingrese la altura (h): "))
        
        # Calcular y mostrar el área
        area = calcular_area_trapecio(base_mayor, base_menor, altura)
        
        print("\nResultado:")
        print(f"Área del trapecio = {area}")
        
    except ValueError as e:
        if str(e) == "Todas las dimensiones deben ser positivas":
            print(f"Error: {e}")
        else:
            print("Error: Por favor, ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")