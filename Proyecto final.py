# Tomas Dolado - AL03026542
# Luis Marcelo - AL03035751

# ----------------------------------- Introduccion -----------------------------------

print("=====================================================================================")
print("Calculadora de costo beneficio para diversos productos dentro de un supermercado/empresa,\nestableciendo los precios de compra al proveedor y los precios de venta al consumidor,\npodras ingresar el producto y se calculara la compra/venta por kilogramo")
print("=====================================================================================\n")

# clase del producto, q es la parte mas complicada de todo creo yo

class Productos:
    
    def __init__(self):
        self.menu = {}
    
    # agregar producto y sus propiedades de precio
    def add_item(self, item, precio_compra, precio_venta):
        self.menu[item] = {'precio_compra': precio_compra, 'precio_venta': precio_venta}
    
    # funcion para remover el item de la lista de productos
    def remove_item(self, item):
        if item in self.menu:
            del self.menu[item]
    
    # funcion para modificar un item, cambiar nombre, precios, etc
    def modify_item(self, old_item, new_item, new_precio_compra, new_precio_venta):
        # definimos como eliminar el item
        if old_item in self.menu:
            del self.menu[old_item]  # item a reemplazar
            self.add_item(new_item, new_precio_compra, new_precio_venta)  # establecemos el nuevo item y los nuevos precios
    
    # funcion para modificar solo el precio de compra o el de venta
    def modify_price(self, item, nuevo_precio_compra=None, nuevo_precio_venta=None):
        if item in self.menu:
            if nuevo_precio_compra is not None:
                self.menu[item]['precio_compra'] = nuevo_precio_compra  # modificamos el precio de compra si se proporciona
            if nuevo_precio_venta is not None:
                self.menu[item]['precio_venta'] = nuevo_precio_venta  # modificamos el precio de venta si se proporciona
    
    # simplificamos para despues y creamos una funcion para poder mostrar el menu mas facil
    def show_menu(self):
        print("\nLa lista de productos es:")  # simple declaracion
        for item, precios in self.menu.items():
            print(f"{item}: Compra - ${precios['precio_compra']:.2f}, Venta - ${precios['precio_venta']:.2f}")
        print()
    
    # Contar items
    def count_items(self):
        return len(self.menu)

# le asignamos una variable a nuestra class

supermercado = Productos()

# Bucle general
while True:
    try:
        # Opciones

        print("==============")
        print("Menu principal")
        print("==============\n")
        print("--- OPCIONES ---\n")

        #Lista de opciones

        print("1. Agregar productos a la lista\n\n2. Eliminar productos de la lista\n\n3. Reemplazar algun elemento\n\n4. Modificar precios de un elemento\n\n5. Mostrar la lista actual de productos y sus precios\n\n6. Finalizar la edicion de lista\n\n6. Salir del programa\n")
        
        opcion = input("¿Que desea hacer?\n- ").lower()  # cambiamos todo a minusculas para evitar problemas

        # Opcion 1: ----------------------------------- AGREGAR PRODUCTOS -----------------------------------

        if opcion in ["1", "agregar", "agregar productos"]:  # asi es mas facil testear los tipos de respuesta
            print("\n===========================")
            print("Menu para agregar productos")
            print("===========================")
            productos_agregar = int(input("\n¿Cuantos productos desea agregar?\n- "))  # vemos la cantidad de productos a agregar

            for i in range(productos_agregar):  # bucle para hacerlo un poco mas facil para el usuario
                add = input("\nProporciona el producto a agregar\n- ").lower()  # determinamos el item a agregar
                precio_compra = float(input(f"\nProporciona el precio de compra por kg para {add}\n- "))  # establecemos tanto precio de compra como precio de venta
                precio_venta = float(input(f"\nProporciona el precio de venta por kg para {add}\n- ")) 

                supermercado.add_item(add, precio_compra, precio_venta)  # lo agregamos a la lista

            supermercado.show_menu()  # mostramos el menu actualizado

            print("------------ Fin del apartado de agregar ------------\n")

        # Opcion 2: ----------------------------------- ELIMINAR PRODUCTOS -----------------------------------

        elif opcion in ["2", "eliminar", "eliminar productos"]:
            print("\n============================")
            print("Menu para eliminar productos")
            print("============================")
        
            if supermercado.count_items() == 0:
                print("\nNo hay productos en la lista.\n")
            else:
                supermercado.show_menu()  # mostramos el menu actual para refrescar la memoria
                productos_remover = int(input("¿Cuantos productos desea remover?\n- "))  # seleccionamos la cantidad de items a remover

                # bucle para hacerlo mas facil para el usuario
                for i in range(productos_remover):
                    remove = input("\nProporciona el nombre del producto que deseas eliminar\n- ").lower()  # determinamos el item a remover del menu
                    supermercado.remove_item(remove)  # removemos por nombre
                supermercado.show_menu()  # volvemos a mostrar el menu actualizado

            print("------------ Fin del apartado para eliminar ------------\n")

        # Opcion 3: -----------------------------------MODIFICAR ELEMENTO (NOMBRE Y PRECIOS) -----------------------------------

        elif opcion in ["3", "modificar", "modificar productos"]:
            if supermercado.count_items() == 0:
                print("\nNo hay productos en la lista.\n")
            else:
                # Solicitamos variables

                supermercado.show_menu()  # mostramos
                # elegimos el item para modificar
                modificar = input("\nElemento a modificar\n- ").lower()
                # pedimos el nuevo elemento
                modificado = input("\nPor que elemento deseas reemplazarlo?\n- ").lower()
                # establecemos el precio de compra
                nuevo_precio_compra = float(input(f"\nNuevo precio de compra por kg para {modificado}\n- "))
                # establecemos el precio de venta
                nuevo_precio_venta = float(input(f"\nNuevo precio de venta por kg para {modificado}\n- "))

                # modificamos el item con todo lo nuevo que nos dieron - Ejecutando las funciones que establecimos en el class
                supermercado.modify_item(modificar, modificado, nuevo_precio_compra, nuevo_precio_venta)
                supermercado.show_menu()  # y mostramos nuevamente para que el usuario vea lo que hizo

            print("------------ Fin del apartado para modificar ------------\n")

        # Opcion 4: ----------------------------------- MODIFICAR SOLO EL PRECIO DE UN ELEMENTO -----------------------------------

        elif opcion in ["4", "modificar precios", "precios"]:
            if supermercado.count_items() == 0:
                print("\nNo hay productos en la lista.\n")
            else:
                supermercado.show_menu()  # mostramos el menu actual
                modificar = input("\nElemento cuyo precio deseas modificar\n- ").lower()  # producto al que se le cambiara el precio

                # Opcion para modificar precio de compra, venta o ambos
                cambio_precio_compra = input("¿Deseas cambiar el precio de compra? (si/no)\n- ").lower()
                nuevo_precio_compra = None
                if cambio_precio_compra == "si":
                    nuevo_precio_compra = float(input(f"\nNuevo precio de compra por kg para {modificar}\n- "))

                cambio_precio_venta = input("¿Deseas cambiar el precio de venta? (si/no)\n- ").lower()
                nuevo_precio_venta = None
                if cambio_precio_venta == "si":
                    nuevo_precio_venta = float(input(f"\nNuevo precio de venta por kg para {modificar}\n- "))

                supermercado.modify_price(modificar, nuevo_precio_compra, nuevo_precio_venta)
                supermercado.show_menu()  # mostramos nuevamente el menu con los cambios

            print("------------ Fin del apartado para modificar precios ------------\n")
        
        # ----------------------------------- MOSTRAR LISTA DE PRODUCTOS -----------------------------------

        elif opcion in ["5", "mostrar", "mostar lista", "mostrar lista actual"]:
            if supermercado.count_items() == 0:
                print("\nNo hay productos en la lista.\n")
            else:
                supermercado.show_menu()
        
        # ----------------------------------- PASAR A LA CALCULADORA -----------------------------------
        elif opcion in ["6", "finalizar"]:
            break

        # ---------------------------------- SALIR DEL PROGRAMA -----------------------------------

        elif opcion in ["7", "salir"]:
            print("\n---------------------------- Fin del programa ----------------------------\n")
            exit()

        # ----------------------------------- EN CASO DE USAR UNA OPCION NO VALIDA -----------------------------------
        else:
            print("\nOpcion no valida. Por favor, elija una opcion correcta.\n")
    
    # ------------ Excepciones ------------

    except KeyboardInterrupt:
        print("No uses Ctrl + C")
    except EOFError:
        print("Tampoco esto")
    except:
        print("Error en el imput")

# Aqui comienza la calculadora de costo-beneficio

# ----------------------------------- Costo Beneficio -----------------------------------
while(True):
    try:
        print("==============================")
        print("Calculadora de Costo-Beneficio")
        print("==============================")

        # definimos la lista de los productos seleccionados
        productos_seleccionados = []

        # mostramos el menu de opciones al usuario
        print("\nOpciones:\n")
        print("1. Calcular costo beneficio para productos especificos")
        print("2. Calcular costo beneficio para todos los productos")
        opcion = input("Seleccione una opcion: ")

        opcion = opcion.lower()
        print(opcion)

        if opcion in ["1", "productos especificos", "especificos"]:
            # mostramos los productos disponibles
            print("\nProductos disponibles:")
            for i, item in enumerate(supermercado.menu, start=1):
                print(f"{i}. {item}")
            
            # pedimos al usuario que seleccione productos
            seleccion = input("Ingrese los numeros de los productos que desea calcular separados por comas y sin espacios: ")
            indices_seleccionados = seleccion.split(',')
            
            # agregamos los productos seleccionados a la lista
            for indice in indices_seleccionados:
                indice = int(indice) - 1
                productos_seleccionados.append(list(supermercado.menu.keys())[indice])

        elif opcion in ["2", "todos los productos", "todos"]:
            productos_seleccionados = list(supermercado.menu.keys())

        else:
            print("Opcion no valida.")
            continue

        for item in productos_seleccionados:
            precio_compra = supermercado.menu[item]['precio_compra']
            precio_venta = supermercado.menu[item]['precio_venta']
            ganancia = precio_venta - precio_compra
            print(f"\nProducto: {item}\nPrecio de compra por kg: ${precio_compra:.2f}\nPrecio de venta por kg: ${precio_venta:.2f}\nGanancia por kg: ${ganancia:.2f}")

        continuar = input("\n¿Desea hacer otro calculo? (si/no): ").lower()
        if continuar == "no":
            print("---------------------------- Fin del programa ----------------------------")
            break

    # ----------- QUE HACER EN CASO DE QUE SALGA UN ERROR -----------
    except KeyboardInterrupt:
        print("No uses Ctrl + C")
    except EOFError:
        print("Tampoco esto")
    except:
        print("Error en el imput")

#Fin del programa
