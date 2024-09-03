# Preimero
print("En este apartado vamos a saludar\n")

def saludo(nombre):
    print(f"Hola {nombre}!")

nombre = input("Como te llamas? ")

saludo(nombre)

# Segundo
print("\nEn este apartado vamos a calcular el area de un circulo en base al radio proporcionado\n")

def area_circulo(radio):
    area = 3.14*radio**2
    print(f"El area de tu circulo es {area}m^2")

radio = float(input("Proporciona el radio de tu circulo"))

area_circulo(radio)

# Tercero
print("\nEn esta parte vamos a convertir millas a kilometros\n")

def millasKilometros(millas):
    kilometros = millas*1.60934
    print(f"{millas} milla/s equivale a {kilometros} kilometro/s")

millas = float(input("Proporciona las millas "))

millasKilometros(millas)

#Cuarto

print("\nEn este apartado vamos a solicitar un texto y una cantidad de veces que luego vamos a usar para imprimir el nombre esa cantidad de veces\n")

def repetirTexto(texto, veces):
    for i in range(veces):
        print(texto)

texto = input("Proporciona tu texto ")
veces = int(input("Cuantas veces quieres repetirlo? "))

repetirTexto(texto, veces)

# Quinto

print("\nEn este apartado vamos a multiplicar 2 numeros y a imprimir su resultado en pantalla\n")

def multiplicar(a,b):
    resultado = a*b
    print(f"El resultado de la multiplicacion de tus numeros es {resultado}")

a = int(input("Proporciona el primero numero "))
b = int(input("Proporciona el segundo numero "))

multiplicar(a,b)


# Sexto

print("\nEn este apartado vamos a solicitar un texto y vamos a cambiar las letras, si estan en minusculas se van a convertir en mayusculas y viceversa\n")

def alternar(cambiarTexto):
    textoAlternado = ""

    #bucle para convertir cada letra pro separado

    for letra in cambiarTexto:

        if letra.islower():  #el caracter es minúscula

            textoAlternado += letra.upper()  # convertir a mayuscula y agregar a la nueva cadena

        elif letra.isupper():  # si el caracter es mayuscula

            textoAlternado += letra.lower()  # convertir a minuscula y agregar a la nueva cadena
        else:
            textoAlternado += letra  # si no es letra agregar el caracter sin cambios
        
    print(f"Tu texto alternado es {textoAlternado}")

cambiarTexto = input("Proporciona tu texto ")

alternar(cambiarTexto)

# Septimo

print("\nEn este apartado vamos a calcular el perimetro de un rectangulo\n")

def perimetroRectangulo(largo, ancho):
    perimetro = 2 * (largo + ancho)
    print(f"El perimetro de tu rectangulo es {perimetro}")

largo = float(input("Proporciona el largo de tu rectangulo "))
ancho = float(input("Proporciona el ancho de tu rectangulo "))

perimetroRectangulo(largo, ancho)

# Octavo

print("\nEn este apartado vamos a calcular la temperatura media de un dia basados en la temperatura maxima y la temperatura minima\n")

def tempMed(max, min):
    temperaturaMedia = (max + min) / 2
    return temperaturaMedia 

def calcularTemp(dias):
    for i in range(dias):
        max = float(input(f"Proporciona la temperatura máxima del día {i+1}: "))
        min = float(input(f"Proporciona la temperatura mínima del día {i+1}: "))
        temperaturaMedia = tempMed(max, min)
        print(f"La temperatura media del día {i+1} es de {temperaturaMedia:.2f} grados") 

dias = int(input("Proporciona la cantidad de días que quieres evaluar: "))

calcularTemp(dias)
