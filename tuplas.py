#creacion de una tupla
tupla = (10,20,30,40,50)

def imprimir_tupla():
    #imprimir una termino en una tupla
    print(f"{tupla[2]} \n")

def tupla_anidada():
    #tupla anidada
    tupla_anidada = ((1,2,3),(4,5,6),(7,8,9))
    print(tupla_anidada[1][1])
    print()#espaciador

def concatenacion_tuplas():
    #concatenacion de tuplas
    tupla_par = (2,4,6,8,10)
    tupla_impar = (1,3,5,7,9)
    concatenacion = tupla_par+tupla_impar
    print(concatenacion, end=" ")

def conteo_elementos():
    #conteo de elementos
    colores = ('rojo', 'azul', 'verde', 'rojo', 'amarillo', 'rojo')
    cont = 0
    for color in colores:
        if color == "rojo":
            cont += 1
        else:
            continue
    print(f"\n\nEl color rojo aparece {cont} veces\n")

def conversion_lista_tuplas():
    #conversion de lista a tuplas
    nombres = ['Ana', 'Juan', 'Pedro', 'Luis']
    nombres = tuple(nombres)

    print(f"La lista ahora es una tupla, se puede comprobar con {type(nombres)}\n")

def slicing_tuplas():
    #Slicing en tuplas
    tupla_larga = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tupla_media = []

    for i in tupla_larga:
        if i <= 5:
            tupla_media.append(i)
        else:
            tupla_media = tuple(tupla_media)
            break
    print(f"{type(tupla_media)}\n")

def intercambio_valores():
    #intercambio d valores
    a = 5
    b = 10

    print(f"Normal {a}, {b}")
    
    a, b = b, a
    tupla_inversa = (a, b)

    print(f"Tupla invertida {tupla_inversa}")

while True:
    print("1.Imprimir una tupla\n2.Mostrar como anidar una tupla\n3.Mostrar una concatenacion de tuplas\n4.Contar los elementos de una tupla\n5.Convertir una lista a tuplas\n6.Siling de tuplas\n7.Intercambiar valores en una tupla")
    opcion = int(input("Que quieres hacer?: "))

    if opcion == 1:
        print()
        imprimir_tupla()

    elif opcion == 2:
        print()
        tupla_anidada()

    elif opcion == 3:
        print()
        concatenacion_tuplas()

    elif opcion == 4:
        print()
        conteo_elementos()

    elif opcion == 5:
        print()
        conversion_lista_tuplas()

    elif opcion == 6:
        print()
        slicing_tuplas()

    elif opcion == 7:
        print()
        intercambio_valores()

    else:
        print()
        print("---------------------- FIN DEL PROGRAMA ----------------------")
        break