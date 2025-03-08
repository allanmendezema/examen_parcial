# trapecio.py
import math

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

def calcular_perimetro_trapecio(base_mayor, base_menor, lado_izquierdo, lado_derecho):
    """
    Calcula el perímetro de un trapecio sumando todos sus lados
    
    Parámetros:
    base_mayor (float): Base mayor del trapecio (B)
    base_menor (float): Base menor del trapecio (b)
    lado_izquierdo (float): Longitud del lado izquierdo del trapecio
    lado_derecho (float): Longitud del lado derecho del trapecio
    
    Retorno:
    float: Perímetro del trapecio
    """
    if base_mayor <= 0 or base_menor <= 0 or lado_izquierdo <= 0 or lado_derecho <= 0:
        raise ValueError("Todas las dimensiones deben ser positivas")
    
    perimetro = base_mayor + base_menor + lado_izquierdo + lado_derecho
    return perimetro

def calcular_perimetro_trapecio_isosceles(base_mayor, base_menor, altura):
    """
    Calcula el perímetro de un trapecio isósceles (lados no paralelos iguales)
    
    Parámetros:
    base_mayor (float): Base mayor del trapecio (B)
    base_menor (float): Base menor del trapecio (b)
    altura (float): Altura del trapecio (h)
    
    Retorno:
    float: Perímetro del trapecio isósceles
    """
    if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
        raise ValueError("Todas las dimensiones deben ser positivas")
    
    # Calcular la longitud de cada lado no paralelo usando el teorema de Pitágoras
    diferencia_bases = abs(base_mayor - base_menor) / 2
    lado_no_paralelo = math.sqrt(diferencia_bases**2 + altura**2)
    
    perimetro = base_mayor + base_menor + 2 * lado_no_paralelo
    return perimetro

# Si se ejecuta este archivo directamente, solicitar entrada del usuario
if __name__ == "__main__":
    try:
        print("Calculadora de Trapecio")
        print("----------------------")
        print("1. Calcular área")
        print("2. Calcular perímetro (trapecio general)")
        print("3. Calcular perímetro (trapecio isósceles)")
        
        opcion = int(input("\nSeleccione una opción (1-3): "))
        
        if opcion == 1:
            # Cálculo del área
            base_mayor = float(input("Ingrese la base mayor (B): "))
            base_menor = float(input("Ingrese la base menor (b): "))
            altura = float(input("Ingrese la altura (h): "))
            
            resultado = calcular_area_trapecio(base_mayor, base_menor, altura)
            print(f"\nEl área del trapecio es: {resultado}")
            
        elif opcion == 2:
            # Cálculo del perímetro (trapecio general)
            base_mayor = float(input("Ingrese la base mayor (B): "))
            base_menor = float(input("Ingrese la base menor (b): "))
            lado_izquierdo = float(input("Ingrese el lado izquierdo: "))
            lado_derecho = float(input("Ingrese el lado derecho: "))
            
            resultado = calcular_perimetro_trapecio(base_mayor, base_menor, lado_izquierdo, lado_derecho)
            print(f"\nEl perímetro del trapecio es: {resultado}")
            
        elif opcion == 3:
            # Cálculo del perímetro (trapecio isósceles)
            base_mayor = float(input("Ingrese la base mayor (B): "))
            base_menor = float(input("Ingrese la base menor (b): "))
            altura = float(input("Ingrese la altura (h): "))
            
            resultado = calcular_perimetro_trapecio_isosceles(base_mayor, base_menor, altura)
            print(f"\nEl perímetro del trapecio isósceles es: {resultado}")
            
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
            
    except ValueError as e:
        if "Todas las dimensiones deben ser positivas" in str(e):
            print(f"Error: {e}")
        else:
            print("Error: Por favor, ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")