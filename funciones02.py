print("Mauricio Antonio Maravilla Herrera")
print("USTR027224")

def verificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

num = int(input("Introduce un número: "))
print(f"El número {num} es: {verificar_numero(num)}")