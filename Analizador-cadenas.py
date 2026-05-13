class AnalizadorDeCadenas:
    def __init__(self):
        self.lista_cadenas = []

    def capturar_datos(self):
        cantidad = int(input("¿Cuántas cadenas deseas ingresar?: "))
        for i in range(cantidad):
            self.cadena = input(f"Ingresa la cadena #{i + 1}: ")
            self.lista_cadenas.append(self.cadena)


    def obtener_cadena_mas_larga(self):
        mas_larga = max(self.lista_cadenas, key=len) 
        return mas_larga
    #El max() busca el maximo, min() el minio, sort() lo acomoda depende el parametro

    def mostrar_resultado(self):
        print("Resultados")
        print(f"Lista completa: {self.lista_cadenas}")
        resultado = self.obtener_cadena_mas_larga()
        print(f"La cadena más larga es: '{resultado}'")
 
 #Use el init aqui para probar       
if __name__ == "__main__":
    analizador = AnalizadorDeCadenas()
    analizador.capturar_datos()
    analizador.mostrar_resultado()