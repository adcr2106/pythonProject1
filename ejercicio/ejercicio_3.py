if __name__ == "__main__":
    import random
    lista = []
    for i in range(1, 11):
        lista.append(random.randint(0, 100))
        unicos = list(dict.fromkeys(lista))
    print(lista)
