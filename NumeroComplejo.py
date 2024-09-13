class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {-self.imaginario}i"

    def sumar(self, otro):
        return NumeroComplejo(self.real + otro.real, self.imaginario + otro.imaginario)

    def restar(self, otro):
        return NumeroComplejo(self.real - otro.real, self.imaginario - otro.imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def dividir(self, otrobobo):
        denominador = otrobobo.real ** 2 + otrobobo.imaginario ** 2
        real = (self.real * otrobobo.real + self.imaginario * otrobobo.imaginario) / denominador
        imaginario = (self.imaginario * otrobobo.real - self.real * otrobobo.imaginario) / denominador
        return NumeroComplejo(real, imaginario)

    def conjugado(self):
        return NumeroComplejo(self.real, -self.imaginario)

    # Método de Newton para la raíz cuadrada sin usar math.sqrt()
    def raiz_cuadrada(self, x, tolerancia=0.0001):
        raiz = x / 2.0
        while abs(raiz * raiz - x) > tolerancia:
            raiz = (raiz + x / raiz) / 2.0
        return raiz

    # Calcular magnitud sin abs()
    def magnitud(self):
        return self.raiz_cuadrada(self.real**2 + self.imaginario**2)

    # Aproximación de arctan sin usar math.atan()
    def arctan_approx(self, y, x):
        if x == 0 and y == 0:
            return 0
        elif x == 0:
            return 90 if y > 0 else 270
        elif y == 0:
            return 0 if x > 0 else 180
        
        # Aproximación simple de arctan basada en relación entre y y x
        approx = y / x
        if x > 0:
            return approx / (1 + 0.28 * approx * approx) * 45  # Aproximación simple de atan
        else:
            if y >= 0:
                return 180 + (approx / (1 + 0.28 * approx * approx) * 45)  # π + atan para cuadrante 2
            else:
                return -180 + (approx / (1 + 0.28 * approx * approx) * 45)  # -π para cuadrante 3

    def angulo_en_grados(self):
        return self.arctan_approx(self.imaginario, self.real)

    def angulo_en_radianes(self):
        grados = self.angulo_en_grados()
        return grados * (3.14159265358979 / 180)

    def a_forma_polar_grados(self):
        magnitud = self.magnitud()
        angulo = self.angulo_en_grados()
        return (magnitud, angulo)

    def a_forma_polar_radianes(self):
        magnitud = self.magnitud()
        angulo = self.angulo_en_radianes()
        return (magnitud, angulo)

    def graficar_binomico(self):
        print(f"({self.real}, {self.imaginario})")

    def graficar_polar(self):
        magnitud, angulo = self.a_forma_polar_grados()
        print(f"Gráfico polar:")
        print(f"   Magnitud: {magnitud}")
        print(f"   Ángulo: {angulo}°")
        print(f"   Coordenadas polares (r = {magnitud}, θ = {angulo}°)")
        print("   +-------------+")
        print("   |             |")
        print(f"   |     *       | (r = {magnitud})")
        print("   |             |")
        print("   +-------------+")

def pedir_numero_complejo():
    real = float(input("Ingrese la parte real del número complejo: "))
    imaginario = float(input("Ingrese la parte imaginaria del número complejo: "))
    return NumeroComplejo(real, imaginario)

def main():
    print("Prueba 1")

    z = pedir_numero_complejo()

    print(f"Tu número en forma binómica es: {z}")

    magnitud_grados, angulo_grados = z.a_forma_polar_grados()
    print(f"Forma polar (grados): Magnitud = {magnitud_grados}, angulo = {angulo_grados}°")

    magnitud_radianes, angulo_radianes = z.a_forma_polar_radianes()
    print(f"Forma polar (radianes): Magnitud = {magnitud_radianes}, angulo = {angulo_radianes} rad")

    print("\nGráfica binómica:")
    z.graficar_binomico()

    print("\nGráfica en polar:")
    z.graficar_polar()

main()
