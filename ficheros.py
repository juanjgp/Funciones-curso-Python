SALIDA = "SALIR"
LISTA = "LISTA"

def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir o {} para ver la lista de productos disponibles para comprar] ".format(SALIDA, LISTA))

def guardar(lista_compra,nombre):
    with open(nombre + ".txt", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def main():
    lista_previa = ["pan", "pollo", "pipas"]
    lista_compra = []

    input_usuario = preguntar_producto_usuario()

    if input_usuario == LISTA:
        print("La lista de productor predefinidos es:")
        for j in lista_previa:
            print(j)
    elif input_usuario == SALIDA:
        print("Pues ha usté a la mierda")
        exit()

    input_usuario = preguntar_producto_usuario()
    while input_usuario != SALIDA:
        #for i in lista_previa:
        if input_usuario in lista_previa:
            lista_compra.append(input_usuario)
            print("\n".join(lista_compra))
            input_usuario = preguntar_producto_usuario()
        else:
            print("Producto no valido")
            input_usuario = preguntar_producto_usuario()

    nombre = input("¿Cuál es el nombre del archivo a guardar?: ")
    guardar(lista_compra, nombre)


if __name__ == "__main__":
    main()