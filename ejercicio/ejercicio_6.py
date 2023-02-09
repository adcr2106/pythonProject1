if __name__ == "__main__":
    lista_de_numeros = [12, 1, 2, 3, 4, 6, 6, 7]
    suma = 0
    x = 0
    while x < len(lista_de_numeros):
        suma = suma + lista_de_numeros[x]
        x = x + 1
    print(suma)