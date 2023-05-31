# Operadores
# Son caracteres para realizar operaciones matematicas

x = int(7)
y = int(2)

suma = x + y
resta = x - y
multi = x * y
division = x / y
division_entera = x // y
modulo = x % y      # Cociente resultado
potencia = x ** y

print(">>> Concatenar con coma <<<")
print("Suma:",suma)
print("Resta:",resta)
print("Multiplicación:",multi)
print("division:",division)
print("division_entera :", division_entera)
print("modulo:",modulo)     # devuelve el residuo de la division
print("potencia:",potencia)


# se usa con directorios
print(">>> Concatenar con formato F <<<")
print(f"Suma:{ suma }")
print(f"Resta:{resta}")
print(f"Multiplicación:{multi}")
print(f"division:{division}")
print(f"division_entera { division_entera}:")
print(f"modulo:{modulo}")    # devuelve el residuo de la division
print(f"potencia:{potencia}")

# se usa en base de datos
print(">>> Concatenar con Format <<<")
print("Suma:{}".format(suma))
print("Resta:{}".format(resta))
print("Multiplicación:{}".format(multi))
print("division:{}".format(division))
print("division_entera:{}".format(division_entera) )
print("modulo:{}".format(modulo))     # devuelve el residuo de la division
print("potencia:{}".format(potencia))