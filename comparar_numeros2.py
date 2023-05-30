# Metodo
def comparar_numeros():
    try: 
        # Solicitar 3 números
        num1 = int(input("Ingrese el primer numero: ")) # 10
        num2 = int(input("Ingrese el segundo numero: ")) # 3
        num3 = int(input("Ingrese el tercer numero: ")) # 9

        # Si 2 o 3 números son iguales, detener ...
        if num1 == num2 or num1 == num3 or num2 == num3:
            print("Hay números que son iguales")
            return

        # Minimo y Maximo con IF
        # if num1 < num2 and num1 < num3:
        #     minimo = num1
        #     if num2 < num3:
        #         medio = num2
        #         maximo = num3
        #     else:
        #         medio = num3
        #         maximo = num2
        # elif num2 < num1 and num2 < num3:
        #     minimo = num2
        #     if num1 < num3:
        #         medio = num1
        #         maximo = num3
        #     else:
        #         medio = num3
        #         maximo = num2
        # else:
        #     minimo = num3
        #     if num1 < num2:
        #         medio = num1
        #         maximo = num2
        #     else:
        #         medio = num2
        #         maximo = num1
        if num1>num2:
            medio = num1
            temp = num2
        else:
            medio = num2
            temp = num1
        if medio > num3:
            medio = num3
        if medio < temp :
            medio = temp

            

        # minimo = min(num1, num2, num3)
        # maximo = max(num1, num2, num3)

        # Determinar cual esta en medio
        # medio = (num1 + num2 + num3) - (minimo + maximo)

        # Imprimir los resultados
        # print(f"el mas grande es: {maximo}")
        print(f"el del medio es: {medio}")
        # print(f"el mas chico es: {minimo}")

    except Exception: 
        print("Se ingreso un valor que no es valido")

# Invocar metodo
comparar_numeros()



