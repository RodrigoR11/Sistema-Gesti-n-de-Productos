productos = []

def añadir_producto():
    # Validación del nombre
    while True:
        nombre = input("Nombre del producto: ")
        if nombre.isalpha():  
            break
        else:
            print("Error: El nombre debe contener solo caracteres alfabéticos. Inténtalo nuevamente.")
    
    # Validación del precio
    while True:
        try:
            precio = int(input("Precio del producto: "))
            if precio > 0:  
                break
            else:
                print("El precio debe ser un número entero positivo.")
        except ValueError:
            print("Error: El precio debe ser un número entero. Inténtalo nuevamente.")
    
    # Validación de la cantidad
    while True:
        try:
            cantidad = int(input("Cantidad del producto: "))
            if cantidad >= 0:  
                break
            else:
                print("La cantidad debe ser un número entero no negativo.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero. Inténtalo nuevamente.")
    
    # Agregar el producto al catálogo
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido exitosamente.")

def ver_productos():
    if not productos:
        print("No hay productos en el sistema.")
        return
    
    for idx, producto in enumerate(productos, start=1):
        print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    indice = int(input("Selecciona el número del producto que quiere actualizar: ")) - 1
    
    if 0 <= indice < len(productos):
        print("Deja el campo en blanco si no deseas cambiar el valor.")
        
        nombre = input(f"Nuevo nombre ({productos[indice]['nombre']}): ")
        precio = input(f"Nuevo precio ({productos[indice]['precio']}): ")
        cantidad = input(f"Nueva cantidad ({productos[indice]['cantidad']}): ")

        if nombre:
            productos[indice]['nombre'] = nombre
        if precio:
            productos[indice]['precio'] = float(precio)
        if cantidad:
            productos[indice]['cantidad'] = int(cantidad)
        
        print("El producto se actualizó exitosamente.")
    else:
        print("El número de producto no es válido.")

def eliminar_producto():
    ver_productos()
    indice = int(input("Por favor seleccione el número del producto que deseas eliminar: ")) - 1
    
    if 0 <= indice < len(productos):
        eliminado = productos.pop(indice)
        print(f"Producto '{eliminado['nombre']}' eliminado exitosamente.")
    else:
        print("Número de producto no válido.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"Producto: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
    print("Datos guardados en 'productos.txt'.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                nombre = datos[0].split(": ")[1]
                precio = datos[1].split(": ")[1]
                cantidad = datos[2].split(": ")[1]
                productos.append({
                    'nombre': nombre,
                    'precio': int(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'. Se creará al guardar.")
    except ValueError:
        print("Error en el formato de datos en 'productos.txt'.")

def menu():
    cargar_datos()  # Cargar datos al iniciar el programa
    while True:
        print("\n    SISTEMA GESTION DE PRODUCTOS    ")
        print("Lista de opciones")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos")

        opcion = input("Ingrese el número de la opción que desea operar: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.(del 1 al 5)")

# Ejecutar el menú
menu()
 