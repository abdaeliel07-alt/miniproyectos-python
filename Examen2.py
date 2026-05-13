class Vectores():
    A = []
    B = []
    C = []
    promedio = 0

    def V1(self):
        self.N1 = 0
        self.N1 = int(input("Cuantos datos: "))
        for i in range(self.N1):
            self.datoA = int(input(f"Agrega el dato: "))
            self.A.append(self.datoA)

    def V2(self):
        self.N2 = 0
        self.N2 = int(input("Cuantos datos: "))
        for j in range(self.N2):
            self.datoB = int(input(f"Agrega el dato: "))
            self.B.append(self.datoB)

    def Juntar(self):
        for x in range(self.N1):
            self.C.append(self.A[x])
        for y in range(self.N2):
            self.C.append(self.B[y])

    def Promedio(self):
        self.N = self.N1 + self.N2
        self.promedio = sum(self.C) / self.N

    def Imprimir(self):
        print(f"El vector A = {self.A}")
        print(f"El vector B = {self.B}")
        print(f"El vector C = {self.C}")
        print(f"El promedio de C es {self.promedio}")

# Segunda hoja
if __name__ == "__main__":
    V = Vectores()
    V.V1()
    V.V2()
    V.Juntar()
    V.Promedio()
    V.Imprimir()