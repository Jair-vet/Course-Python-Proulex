# Ciclo While
# Repetición de Instrucciones mientras se cumpla una condición

# 1) Repetir un proceso hasta que el número sea igual o mayor a lo esperado

numero = 1

while numero <= 100:
    print(numero)
    numero += 1

# 2) Incrementar el valor de x en 10 en 10 hasta 1,000, pero si x llega a 500 que se salga del cico

x = 0

while x <= 1000:
    print(x)
    x += 10
    if x == 500:
        print("X ya vale 500, voy a detener el ciclo")
        break


# 3) solicitar un número, se repetira la instrucción hasta obtener un dato valido y un break cuando
# se cumpla la condición


# Cliclo infinito
while True:
    try:    
        numero = int(input("Ingresa un numero entero: "))
        print("Perfecto, ingresaste una opción valida")
        break
    except ValueError:
        print("Ingresa una opción valida")
        continue