# Metodo
def comparar_numeros():
    try: 
        # Solicitar 3 números
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        num3 = int(input("Ingrese el tercer numero: "))

        # Si 2 o 3 números son iguales, detener ...
        if num1 == num2 or num1 == num3 or num2 == num3:
            print("Hay números que son iguales")
            return

        # Minimo y Maximo
        minimo = min(num1, num2, num3)
        maximo = max(num1, num2, num3)

        # Determinar cual esta en medio
        medio = (num1 + num2 + num3) - (minimo + maximo)

        # Imprimir los resultados
        print(f"el mas grande es: {maximo}")
        print(f"el del medio es: {medio}")
        print(f"el mas chico es: {minimo}")

    except Exception: 
        print("Se ingreso un valor que no es valido")

# Invocar metodo
comparar_numeros()



