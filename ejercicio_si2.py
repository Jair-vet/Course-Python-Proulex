a = 10
b = 20
c = 30


if a!=b and a!=c and b!=c:
    print("Las 3 variables son diferentes")
   
    # Saber cual es la mayor 
    if a>b and a>c:
        print("La A es la más Grande")
    elif b>a and b>c:
        print("La B es la más Grande")
    else:
        print("La C es la más Grande")

    # Saber cual es la menor
    if a<b and a<c:
        print("La A es la Menor")
    elif b<a and b<c:
        print("La B es la Menor")
    else:
        print("La C es la Menor")

elif a==b and a==c and b==c:
    print("Las 3 variables son iguales")
elif a==b and a!=c:
    print("La A y B son iguales, C es diferente")
elif a==c and a!=b:
    print("La A y C son iguales, B es diferente")
elif c==b and a!=c:
    print("La C y B son iguales, A es diferente")

else:
    print("No se cumplen las condiciones")
