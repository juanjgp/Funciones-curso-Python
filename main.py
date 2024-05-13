def saludo_sectario(nombre):
    print("Hola {}".format(nombre[::-1]))

saludo_sectario("Juan José")

def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
    return largo


largo_de_la_string = largo_string("hola mundo")
print(largo_de_la_string)
