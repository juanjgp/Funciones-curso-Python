def main():
    print("multiplicación de una palabra tantas veces como el usuario diga")
    palabra = input(("Escribe una palabra: "))
    repeticiones = int(input("Dime cuántas veces quieres que se repita: "))
    resultado = palabra * repeticiones
    print(resultado)


if __name__ == "__main__":
    main()

def potencia(numero):
    resultado = numero ** 2
    return resultado

numero = int(input("Dime un número y te calculo su potencia: "))

print("La potencia del número elegido es: {}".format(potencia(numero)))