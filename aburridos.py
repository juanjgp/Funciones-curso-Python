def string_mas_larga(string1, string2, string3):
    largo1 = len(string1)
    largo2 = len(string2)
    largo3 = len(string3)
    if largo1 >= largo2 and largo2 >= largo3:
        return string1
    if largo2 >= largo1 and largo1 >= largo3:
        return string2
    if largo3 >= largo2 and largo2 >= largo1:
        return string3


string_mas_larga("Hola", "como", "estás")
print(string_mas_larga("Hola", "como", "estás"))

def suma(numero1, numero2, numero3, numero4, numero5):
    resultado = numero1 + numero2 + numero3 + numero4 + numero5
    return resultado

suma_numeros = print(suma(6, 7, 8,5,3))

def es_impar(numero):
    if numero % 2 == 0:
        valor = False
    else:
        valor = True

    return valor

resultado = print(es_impar(4))

def seguro():
    seguridad = input("¿Estás seguro?: ")
    if seguridad == "si":
        return True
    else:
        return False

print(seguro())


def mayuscula():
    capletras = []
    regletras = []
    mayuscula = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    minuscula = 'abcdefghijklmnñopqrstuvwxyz'
    for x in mayuscula:
        capletras.append(x)
    for x in minuscula:
        regletras.append(x)
    print(capletras, regletras)
    palabra = input('Cual es tu string a convertir?\n')
    nueva_palabra = []
    for x in palabra:
        if x in capletras:
            nueva_palabra.append(x)
        elif x not in capletras and x not in regletras:
            nueva_palabra.append(x)
        else:
            conversion = regletras.index(x)
            if x:
                proc = capletras[conversion]
                nueva_palabra.append(proc)
    resultado = ''.join(nueva_palabra)
    return resultado
print(mayuscula())


def adivina_numero(numero):
    numero_usuario = int(input("Dime el número que estoy pensando del 1 al 10: "))
    while numero_usuario != numero:
        if numero_usuario < 1 or numero_usuario > 10:
            print("Numero incorrecto. es del 1 al 10, tu eres tonto chaval")
            numero_usuario = int(input("Dime el número que estoy pensando del 1 al 10: "))
        elif numero_usuario != numero:
            print("No es el número pensado, sigue intentándolo")
            numero_usuario = int(input("Dime el número que estoy pensando del 1 al 10: "))

    acierto = "Correcto. Estás hecho un máquina"
    return acierto

acierto = adivina_numero(7)

print(acierto)

lista_predefinida = ["leche", "huevos"]

print("Lista predefinida", lista_predefinida)

def lista_compra(lista_predefinida):
    lista_usuario = []
    compra = input("Qué desea añadir a la lista: (salir para acabar) ")
    while compra != "salir":
        for i in lista_predefinida:
            if compra in lista_predefinida:
                print("El producto ya se encuentra en la lista. Coge otro")
                compra = input("Qué desea añadir a la lista: (salir para acabar) ")
            else:
                lista_usuario.append(compra)
                print("producto añadido", lista_usuario)
                compra = input("Qué desea añadir a la lista: (salir para acabar) ")

    return lista_usuario

lista_final = lista_compra(lista_predefinida)

print("La lista final es: ", lista_predefinida + lista_final)