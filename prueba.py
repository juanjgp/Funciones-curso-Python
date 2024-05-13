SALIDA = "SALIR"
LISTA = "LISTA"
lista_previa = ["pan", "pollo", "pipas"]
lista_compra = []
input_usuario = input("Introduce un producto [{} para salir o {} para ver la lista de productos disponibles para comprar] ".format(SALIDA, LISTA))
while input_usuario != SALIDA:
    for i in lista_previa:
        if input_usuario in lista_previa:
            lista_compra.append(input_usuario)
            print("\n".join(lista_compra))
            input_usuario = input("Introduce un producto [{} para salir o {} para ver la lista de productos disponibles para comprar] ".format(SALIDA, LISTA))
        else:
            print("Producto no valido")
            input_usuario = input("Introduce un producto [{} para salir o {} para ver la lista de productos disponibles para comprar] ".format(SALIDA, LISTA))