"""
Algoritmo para sistematizar el cálculo de:
  - Figuras planas: perímetro y área
  - Sólidos regulares: área superficial y volumen

Uso: ejecutar el programa y elegir la figura en el menú.
"""
import math


# ---------- Utilidades ----------
def leer_numero(mensaje):
    """Pide un número positivo y valida la entrada."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if valor > 0:
                return valor
            print("  El valor debe ser mayor que 0.")
        except ValueError:
            print("  Entrada no válida. Escriba un número.")


# Unidades permitidas: lo que el usuario puede escribir -> símbolo que se muestra
UNIDADES = {
    "mm": "mm", "milimetros": "mm", "milímetros": "mm",
    "cm": "cm", "centimetros": "cm", "centímetros": "cm",
    "m": "m", "metros": "m", "metro": "m",
    "km": "km", "kilometros": "km", "kilómetros": "km",
}


def leer_unidad():
    """Pide la unidad de medida. Es obligatoria y debe ser una de las permitidas."""
    while True:
        texto = input("  Unidad de medida (mm, cm, m, km): ").strip().lower()
        if texto == "":
            print("  La unidad es obligatoria. Escriba mm, cm, m o km.")
        elif texto in UNIDADES:
            return UNIDADES[texto]
        else:
            print("  Unidad no válida. Escriba mm, cm, m o km.")


def otra_consulta():
    """Pregunta si desea hacer otra consulta. Devuelve True (sí) o False (no)."""
    while True:
        texto = input("\n¿Quieres realizar otra consulta? (si/no): ").strip().lower()
        if texto in ("si", "sí", "s"):
            return True
        if texto in ("no", "n"):
            return False
        print("  Respuesta no válida. Escriba si o no.")


# ---------- Figuras planas: devuelven (perímetro, área) ----------
def cuadrado(lado):
    return 4 * lado, lado ** 2


def rectangulo(base, altura):
    return 2 * (base + altura), base * altura


def triangulo_equilatero(lado):
    return 3 * lado, (math.sqrt(3) / 4) * lado ** 2


def circulo(radio):
    return 2 * math.pi * radio, math.pi * radio ** 2


def poligono_regular(n, lado):
    perimetro = n * lado
    apotema = lado / (2 * math.tan(math.pi / n))
    return perimetro, perimetro * apotema / 2


# ---------- Sólidos: devuelven (área superficial, volumen) ----------
def cubo(arista):
    return 6 * arista ** 2, arista ** 3


def tetraedro(arista):
    return math.sqrt(3) * arista ** 2, arista ** 3 / (6 * math.sqrt(2))


def octaedro(arista):
    return 2 * math.sqrt(3) * arista ** 2, (math.sqrt(2) / 3) * arista ** 3


def dodecaedro(arista):
    area = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * arista ** 2
    volumen = (15 + 7 * math.sqrt(5)) / 4 * arista ** 3
    return area, volumen


def icosaedro(arista):
    return 5 * math.sqrt(3) * arista ** 2, 5 * (3 + math.sqrt(5)) / 12 * arista ** 3


def esfera(radio):
    return 4 * math.pi * radio ** 2, (4 / 3) * math.pi * radio ** 3


def cilindro(radio, altura):
    return 2 * math.pi * radio * (radio + altura), math.pi * radio ** 2 * altura


def cono(radio, altura):
    generatriz = math.sqrt(radio ** 2 + altura ** 2)
    return math.pi * radio * (radio + generatriz), math.pi * radio ** 2 * altura / 3


# ---------- Tabla de figuras: nombre, función, datos que pide, tipo ----------
FIGURAS = {
    "1": ("Cuadrado", cuadrado, ["lado"], "plana"),
    "2": ("Rectángulo", rectangulo, ["base", "altura"], "plana"),
    "3": ("Triángulo equilátero", triangulo_equilatero, ["lado"], "plana"),
    "4": ("Círculo", circulo, ["radio"], "plana"),
    "5": ("Polígono regular de n lados", poligono_regular, ["número de lados", "lado"], "plana"),
    "6": ("Cubo (hexaedro)", cubo, ["arista"], "sólido"),
    "7": ("Tetraedro regular", tetraedro, ["arista"], "sólido"),
    "8": ("Octaedro regular", octaedro, ["arista"], "sólido"),
    "9": ("Dodecaedro regular", dodecaedro, ["arista"], "sólido"),
    "10": ("Icosaedro regular", icosaedro, ["arista"], "sólido"),
    "11": ("Esfera", esfera, ["radio"], "sólido"),
    "12": ("Cilindro", cilindro, ["radio", "altura"], "sólido"),
    "13": ("Cono", cono, ["radio", "altura"], "sólido"),
}


def mostrar_menu():
    print("\n===== CALCULADORA DE FIGURAS =====")
    print("-- Figuras planas (perímetro y área) --")
    for k, (nombre, _, _, tipo) in FIGURAS.items():
        if tipo == "plana":
            print(f"  {k:>2}. {nombre}")
    print("-- Sólidos (área superficial y volumen) --")
    for k, (nombre, _, _, tipo) in FIGURAS.items():
        if tipo == "sólido":
            print(f"  {k:>2}. {nombre}")
    print("   0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()
        if opcion == "0":
            print("Fin del programa.")
            break
        if opcion not in FIGURAS:
            print("Opción no válida.")
            continue

        nombre, funcion, datos, tipo = FIGURAS[opcion]
        print(f"\n{nombre}")
        unidad = leer_unidad()
        valores = []
        for d in datos:
            if d == "número de lados":
                valores.append(leer_numero(f"  Ingrese {d}: "))
            else:
                valores.append(leer_numero(f"  Ingrese {d} (en {unidad}): "))

        if funcion is poligono_regular and (valores[0] < 3 or valores[0] != int(valores[0])):
            print("  El número de lados debe ser un entero mayor o igual a 3.")
            continue
        if funcion is poligono_regular:
            valores[0] = int(valores[0])

        r1, r2 = funcion(*valores)
        if tipo == "plana":
            print(f"  Perímetro = {r1:.2f} {unidad}")
            print(f"  Área      = {r2:.2f} {unidad}²")
        else:
            print(f"  Área superficial = {r1:.2f} {unidad}²")
            print(f"  Volumen          = {r2:.2f} {unidad}³")

        if not otra_consulta():
            print("Fin del programa. ¡Gracias!")
            break


if __name__ == "__main__":
    main()
