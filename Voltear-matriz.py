class volteo_de_matriz():
    matriz = []
    renglones = 0
    columnas = 0
    def creacion_de_matriz(self):
        self.renglones = int(input('Cuantos renglones: '))
        self.columnas = int(input('Cuantas columnas: '))
        for i in range(self.renglones):
            self.matriz.append([])
            for c in range(self.columnas):
                self.dato = (int(input(f'Agrega el dato en [{i+1}][{c+1}]')))
                self.matriz[i].append(self.dato)
    
    def escribir_matriz(self):
        for a in range(self.renglones):
            print(self.matriz[a])
    
    def escribir_matriz_volteada(self):
        print('Matriz Volteada')
        for c in range(self.columnas):
            self.fila_temporal = []
            for r in range(self.renglones):
                self.fila_temporal.append(self.matriz[r][c])
            print(self.fila_temporal)

            
        







if __name__ == '__main__':
    V = volteo_de_matriz()
    V.creacion_de_matriz()
    V.escribir_matriz()
    V.escribir_matriz_volteada()