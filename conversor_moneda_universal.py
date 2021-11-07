menu = """
Bienvenido

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Argentinos
Elige una opcion: """

opcion = int(input(menu))


def calcular(mensaje, precio_dolar):
    return str(round(float(input(mensaje)) / precio_dolar, 2))


if(opcion == 1):
    print("tienes $" + calcular("Pesos Colobianos: ", 3875) + " Dolar(es)")
elif(opcion == 2):
    print("tienes $" + calcular("Pesos Mexicanos: ", 20) + " Dolar(es)")
elif(opcion == 3):
    print("tienes $" + calcular("Pesos Argentinos: ", 98) + " Dolar(es)")
else:
    print("Ingrese una opcion del menu")
