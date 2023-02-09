if __name__ == "__main__":
    import random
    def matriz_numeros():
        matriz = []
        for fila in range(5):
            matriz.append([])
            for columnas in range(5):
                matriz[fila].append(random.randint(0, 100))
        return matriz


    matriz = matriz_numeros()
    for fila in matriz:
        print(fila)