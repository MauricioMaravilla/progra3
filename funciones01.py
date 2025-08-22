#crear la funcion
def suma(num1,num2):
    return num1 + num2

#solicita la variable
num1 = int(input("introduce el primer numero para sumar: "))
num2 = int(input("introduce el segundo numero para sumar: "))

#imprimir el resultado
print(f"suma de: {num1} + {num2} es: {suma(num1,num2)}")