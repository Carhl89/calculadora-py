def sumar(a, b):
     return a + b
def restar(a, b):
     return a - b
def multiplicar( a, b):
     return a * b
def dividir(a, b):
     return a / b

while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Eligi una opcion: ")
    
    if opcion =="5":
        print("Programa terminado")
        break
    if opcion in ["1", "2","3","4",]:
        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))
    if opcion == "1":
        print("Resultado: ", sumar(num1, num2))
    elif opcion == "2":
        print("Resultado: ",
              restar(num1 ,num2))
    elif opcion == "3":
        print("Resultado: ", multiplicar(num1, num2))
    elif opcion == "4":
        print("Resultado: ", dividir(num1, num2))
    else:
        print("Opsion invalida")