#importo las librerias que voy a usar
import json
import sys

#Despues declaro todas las funciones, la primera funcion servirá
#para llamarla cuando carguemos por primera vez los productos
def load_products():
    try:
        with open('users2.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {'productos': []}
   
   
def insert_product (data):
    name = input('Ingrese el nombre de su producto: ')
    price = int(input ('Ingrese el precio de su producto:'))
    quantity = int(input('Ingrese la cantidad de su producto: ')) 
    description = input ('Ingrese la descripción de su producto: ')
    id = int(input('Ingrese el id de su producto: '))
    
    # mando los datos a una variable
    newProduct = {
             'nombre': name,
             'precio': price,
             'cantidad-stock': quantity,
             'descripcion': description,
             'id': id
             }
   # Verificamos que el producto no existe por ID
    existingId = [product['id'] for product in data['productos']]
    if newProduct['id'] not in existingId:
        data['productos'].append(newProduct)
        print("Nuevo producto agregado exitosamente")
    else:
        print("El producto con el mismo ID ya existe en el archivo JSON.")

    # Guardar el diccionario actualizado en el archivo JSON
    with open('users2.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("La información del usuario ha sido guardada")
  
def edit_product(data):
    
    print(json.dumps(data, indent=4))
    idProduct = int(input('Ingrese el ID del producto que desea editar: '))
    
    try:
        for productos in data['productos']:
            if productos['id'] == idProduct:
                print("solo puede modificar precio y cantidad")
                price = int(input('Ingrese el nuevo precio del producto: '))
                quantity = int(input('Ingrese la nueva cantidad de stock del producto: '))
                
                productos['precio'] = price
                productos['cantidad-stock'] = quantity
                
                with open('users2.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    print("Producto actualizado exitosamente.")
                    return
        print("No se encontró ningún producto con el ID proporcionado.")        
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el ID.")

def delete_product(data):
    idProduct = int(input('Ingrese el ID del producto que desea eliminar: '))
    for product in data['productos']:
        if product['id'] == idProduct:
            data['productos'].remove(product)
            with open('users2.json', 'w') as file:
                    json.dump(data, file, indent=4)
            print("Producto eliminado exitosamente.")
            return
    print("No se encontró ningún producto con el ID proporcionado.")

def search_product(data):
    print("Solo se busca por nombre")
    nameSearch = input('Ingrese el NOMBRE del producto que desea buscar: ')
    foundProducts = []
    
    for product in data['productos']:
        if nameSearch.lower() in product['nombre'].lower():
            foundProducts.append(product)
    
    if foundProducts:
        print("Productos encontrados:")
        for product in foundProducts:
            print(product)
    else:
        print("No se encontraron productos con el nombre proporcionado.")

def show_products(data):
    print("Lista de productos:")
    print('-' * 20)
    for product in data['productos']:
            print(f"ID: {product['id']}")
            print(f"Nombre: {product['nombre']}")
            print(f"Precio: {product['precio']}")
            print(f"Cantidad en stock: {product['cantidad-stock']}")
            print(f"Descripción: {product['descripcion']}")
            print('-' * 20)

#En esta seccion pongo el menu para que elija el usuario
while True:
    print("""
        (1) Agregar prodcutos
        (2) Actualizar prodcutos
        (3) Eliminar prodcutos
        (4) Buscar productos
        (5) Generar informe
        (6) Salir
        """)

#Dependendiendo de la respuesta hago un condicional para llamar a la funcion correcta
    resp = int(input('Ingrese alguna opción: '))
    data = load_products()
    productCount = len(data['productos'])
    
    if resp == 1:
        insert_product(data)
    elif resp == 2:
        if productCount == 0:
            print('Aun no hay productos, elije otra opción')
        else:
            edit_product(data)  
    elif resp == 3:
        if productCount == 0:
            print('Aun no hay productos, elije otra opción')
        else:
            delete_product(data)  
    elif resp == 4:
        if productCount == 0:
            print('Aun no hay productos, elije otra opción')
        else:
            search_product(data)
    elif resp == 5:
        if productCount == 0:
            print('Aun no hay productos, elije otra opción')
        else:
            show_products(data)                     
    elif resp == 6:
        print("Adios")
        sys.exit()

        