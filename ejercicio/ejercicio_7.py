if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7]
    menor = lista[0]
    posicion = 0
    for x in range(1, len(lista)):
        if lista[x] < menor:
            menor = lista[x]
            posicion = x

    mayor = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]

    print("Lista completa")
    print(lista)
    print("-----------------------------------------")
    print("Menor de la lista")
    print(menor)
    print("-----------------------------------------")
    print("Mayor de la lista")
    print(mayor)