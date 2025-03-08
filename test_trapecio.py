# test_trapecio.py
import unittest
from trapecio import calcular_area_trapecio

class TestAreaTrapecio(unittest.TestCase):
    
    def test_area_trapecio_normal(self):
        # Caso de prueba con valores típicos
        resultado = calcular_area_trapecio(8, 6, 4)
        self.assertEqual(resultado, 28)
    
    def test_area_trapecio_valores_decimales(self):
        # Caso de prueba con valores decimales
        resultado = calcular_area_trapecio(5.5, 3.5, 2)
        self.assertEqual(resultado, 9)
    
    def test_area_trapecio_caso_rectangulo(self):
        # Caso donde base mayor = base menor (rectángulo)
        resultado = calcular_area_trapecio(5, 5, 3)
        self.assertEqual(resultado, 15)
    
    def test_valores_negativos(self):
        # Caso con valores negativos (debería lanzar un error)
        with self.assertRaises(ValueError):
            calcular_area_trapecio(-5, 3, 2)
        with self.assertRaises(ValueError):
            calcular_area_trapecio(5, -3, 2)
        with self.assertRaises(ValueError):
            calcular_area_trapecio(5, 3, -2)

# Para ejecutar las pruebas directamente
if __name__ == "__main__":
    unittest.main()