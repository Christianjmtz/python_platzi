lista = [1, 2, 3, 4]
print("FULL")
print(lista)
lista.pop(0)
print("POP")
print(lista)
lista.append(10)
print("APPEND")
print(lista)

est_tupla = (1, 2, 3, 4, 5)  # Es mas rapida que la lista
print("TUPLA")
print(est_tupla)

diccionarios = {
    'propiedad_1': 'valor1',
    'propiedad_2': 'valor2'
}
print("DICCIONARIOS")
print(diccionarios['propiedad_1'])

for llave in diccionarios.keys():
    print(diccionarios[llave])

for llave, valor in diccionarios.items():
    print(llave + ' Tiene el valor: ' + valor)
