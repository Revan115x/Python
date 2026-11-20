# ==============================================================================
# 1. DATOS DE PARTIDA 
# ==============================================================================
categorias_lista= ["Portátiles", "Periféricos", "Monitores", "Almacenamiento","Periféricos","Monitores"]

ids_lista = ["P01", "P02", "P03", "P04", "P05"]

datos_lista = [
    ["Teclado Mecánico", "Periféricos", "60.0", "15"],
    ["Monitor 4K 27\"", "Monitores", "300.0", "5"],
    ["Ratón Inalámbrico", "Periféricos", "25.0", "0"],
    ["Disco SSD 1TB", "Almacenamiento", "80.0", "20"],
    ["Laptop Gaming", "Portátiles", "1200.0", "3"],
]

ventas= [
    ("P01", 2, 10), # Vendidas 2 unidades de P01 con 10% de descuento
    ("P05", 1, 5), 
    ("P01", 1, 0),
    ("P04", 5, 15),
    ("P01", 6, 0),
    ("P03", 2, 0), # Intento de venta sin stock
    ("P06", 3, 5)  # Intento de venta de un producto descatalogado
]

categoria_set = []
catalogo_dict = {}

# ==============================================================================
# 2. FUNCIONES A IMPLEMENTAR 
# ==============================================================================
"""
    A.Convierte las listas iniciales en un conjunto de categorías y un diccionario
    realizando el casting de tipos.
    """
def preparar_estructras(categorias_lista,ids_lista,datos_lista):
    categoria_set = set(categorias_lista)
    print("CATEGORIAS")
    print(categoria_set)

    datos = {
        "nombre" : datos_lista[0][0],"categoria" : datos_lista[0][1],"precio" :float(datos_lista[0][2]),"stock" :int(datos_lista[0][3])
    }   
    catalogo_dict = dict(zip(ids_lista,datos))

    print("CATALOGO")
    for clave,valor in catalogo_dict.items():
        print(clave, "" ,valor)


"""B.1 Devuelve un conjunto con las categorías únicas que tienen al menos una venta efectiva."""


def get_categorias_vendidas(ventas,catelogo_dict):
    print("a")





"""
    B.2 Procesa cada venta, actualiza el stock en el catálogo original y devuelve
    una tupla con (total_recaudado, lista_de_ids_agotados).
    """









"""
    B.3 Calcula el valor monetario total del stock restante agrupado por categoría.
    """







# ==============================================================================
# 3. PROGRAMA PRINCIPAL 
# ==============================================================================

# 1. Preparar estructuras iniciales

preparar_estructras(categorias_lista,ids_lista,datos_lista)



# 2. Obtener categorías con ventas efectivas






# 3. Procesar ventas y actualizar inventario






# 4. Resumen de inventario por categoría