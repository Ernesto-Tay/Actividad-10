productos = []
while True:
    print("\n\n------Lista de acciones-----\n1. Ingresar un producto\n2. Mostrar todos los productos\n3. Buscar un producto\n4. Calcular el inventario\n5. Mostrar los productos por categoría\n6. Salir")
    select = input("Seleccione una opción: ")
    match select:
        case 1:
            while True:
                try:
                    cant = int(input("Cantidad de productos que ingresará: "))
                    if cant<=0:
                        print("Ingrese un valor positivo")
                    else:
                        break
                except:
                    print("Ingrese un número entero")

            for i in cant:
                codigo = input("Ingrese el código del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese la categoria del producto: ")
                talla = input("Ingrese la talla del producto: ")
                while True:
                    try:
                        precio = int(input("Ingrese el precio del producto: "))
                        stock = input("Ingrese el stock del producto: ")
                        if precio <=0:
                            print("El precio debe tener un valor positivo")
                        if stock <=0:
                            print("El stock debe tener un valor positivo")
                        else:
                            break
                    except:
                        print("Ingrese números enteros por favor")

                productos[codigo] = {
                    "nombre": nombre,
                    "categoria": categoria,
                    "talla": talla,
                    "precio": precio,
                    "stock": stock
                }

        case 2:
            if not productos:
                print("No hay productos ingresados")
            else:
                for ID, producto in productos:
                    print(f"\nCodigo: {ID}\nNombre: {producto['nombre']}\nCategoria: {producto['categoria']}\nTalla: {producto['talla']}\nPrecio: {producto['precio']}\nStock: {producto['stock']}")

        case 3:
            if not productos:
                print("No hay productos ingresados")
            else:
                ID_search = input("Ingrese el código del producto que desea buscar: ")
                if ID_search in productos:
                    print(f"\nProducto encontrado\nNombre: {productos[ID_search]['nombre']}\nCategoria: {productos[ID_search]['categoria']}\nTalla: {productos[ID_search]['talla']}\nPrecio: {productos[ID_search]['precio']}\nStock: {productos[ID_search]['stock']}")
                else:
                    print("No se encontrado un producto con ese código")
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Saliendo del programa...")
            break
        case _:
            print("Por favor elija una opción del menú")