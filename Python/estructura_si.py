# estructura de control IF
# Su funcion principal es tomar decisiones y evaluar escenarios atráves de "condiciones"

# if: "evalua lo siguiente y dime si es verdadero o falso"
# elif: "si lo anterior fue falso, entonces evalua lo siguiente"
# else: "Si nada de lo anterior fue verdad entonces ingresa a esta etapa de la estructura"

'''
> mayor que
>= mayor o igual que
< menor que
<= menor o igual que
== igual a, comparación
!= diferente de
And Y
Or O
'''

# Ejemplo 1
if 100 > 10 :
    print("El número 100 es mayor")

# Ejemplo 2
a = 10
b = 20

if a > b: 
    print("La A es menor que B")

# Ejemplo 3
x = 1
y = 1
z = 1

if x > y and x > z :
    print("X es la más grande")
elif y > x and y > z :
    print("Y es la más grande")
elif z > x and z > y :
    print("Z es la más grande")
else:
    print(" Todas las variables son iguales")