#contador = 0
#print('2 elevado a ' + str(contador) + ' es igual a: ' + str(2**contador)) 

def ciclo_while(LIMITE,contador,potencia_2):
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

def ciclo_for():
    for i in range(1,11):
        print(i)

def recorrer_caracteres(palabra):
    for letra in palabra:
        print(letra)

def break_continue():
    # CONTINUE - Brincar ciertos valores dentro del ciclo
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # BREAK
    for i in range(10000):
        print(i)
        if i == 100:
            break # Romper el ciclo cuando se cumpla cierta condicion
        


def run():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2**contador

    # CICLO WHILE
    #ciclo_while(LIMITE,contador,potencia_2)

    #CICLO FOR
    #ciclo_for()

    # RECORRIENDO CARACTERES
    #nombre = input('Escribe tu nombre: ')
    #recorrer_caracteres(nombre)

    # BREAK / CONTINUE
    break_continue()

if __name__ == '__main__':
    run()