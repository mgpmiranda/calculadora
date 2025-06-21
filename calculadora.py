"""
Operación: División |
Este módulo permite realizar la operación de división entre dos números,
validando que sean números válidos y que no se divida entre cero.
"""

def validar_entrada(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (ValueError, TypeError):
            return "Error: Ingrese números válidos"
        except ZeroDivisionError:
            return "Error: No se puede dividir por cero"
    return wrapper

class Calculadora:
    @staticmethod
    @validar_entrada
    def dividir(a, b):
        return float(a) / float(b)

if __name__ == "__main__":
    print("División con validación:")
    try:
        a = float(input("Ingrese el dividendo: "))
        b = float(input("Ingrese el divisor: "))
        resultado = Calculadora.dividir(a, b)
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Por favor ingrese números válidos.")
