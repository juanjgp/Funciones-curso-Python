print("Secuencia de fibonacci con recursividad")

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n - 1) + fib(n - 2)


print(fib(8))

for i in range(10):
    print(fib(i))

print("Secuencia de Fibonacci sin recursividad")
#0 1 1 2 3 5 8 13 21 34 55
class Fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
    def run(self):
        if(self.cantidad <= 2):
            print(0)
            print(1)
        else:
            print(0)
            print(1)
            anterior = 0
            reciente = 1
            for i in range(self.cantidad - 2):
                res = anterior + reciente
                print(res)
                anterior = reciente
                reciente = res


f = Fibonacci(10)
f.run()

print("Potencia con base opcional")


def potencia(numero, base=False):
    if base:
        resultado = numero ** base
    else:
        resultado = numero ** 2

    return resultado

print(potencia(4,3))