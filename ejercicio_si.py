
# Obtener numeros
a = 40
b = 10
c = 10

if a!=b and a!=c and b!=c:
    print("Las 3 Variables son diferentes")
elif a==b and a==c and b==c:
    print("Las 3 Variables son iguales")
elif a==b and a != c:
    print("La A y B son iguales, C es diferente")
elif a==c and a != b:
    print("La A y C son iguales, B es diferente")
elif b==c and a != b:
    print("La B y C son iguales, A es diferente")
elif a>b and a>c:
    print("La A es la mayor")
elif b>a and b>c:
    print("La B es la mayor")
elif c>a and c>b:
    print("La C es la mayor")
else:
    print("No se cumplen las condiciones")