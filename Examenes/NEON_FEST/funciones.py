from exceptions import *

#FUNCIONES AUXILIARES

def validar_dni(dni):
    """Comprueba que el DNI tenga formato válido de 8 números y 1 letra."""
    if len(dni) != 9:
        raise DniInvalidoError("El DNI debe tener 9 caracteres")
    numeros = dni[:8]
    letra = dni[-1]
    
    if not numeros.isdigit():
        raise DniInvalidoError("Los primeros 8 caracteres deben ser números")
    if letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise DniInvalidoError("El último carácter debe ser una letra")
    return True


def validar_entrada(tipo, tipo_entrada):
    """Valida que el tipo de entrada introducido sea correcto."""
    if tipo not in tipo_entrada:
        raise NoFoundTypeEntradaError("El tipo de entrada no es válido")
    return True 


def validar_edad(edad):
    """Comprueba que la edad sea un número entero mayor o igual a 18."""
    if type(edad) != int:
        raise EdadInvalidaError("La edad debe ser un número entero")
    if edad < 18:
        raise EdadInvalidaError("Debe ser mayor de edad para registrarse")
    return True

# OPCIÓN 1: MOSTRAR ENTRADAS

def mostrar_entradas(stock_entradas, precios_entrada):
    """Muestra el catálogo de entradas, sus precios y el stock disponible."""
    print("--- ENTRADAS NEON FEST ---")
    for tipo, precio in precios_entrada.items():
        stock = stock_entradas.get(tipo)
        print("Tipo de entrada:", tipo)
        print("Precio:", precio, "€")
        print("Stock disponible:", stock)


# OPCIÓN 2: COMPRAR ENTRADAS

def comprar_entradas(grupo, asistentes, stock_entradas, precios_entrada):
    """Procesa la compra en lote para un grupo de personas tras validar sus datos."""
    if len(grupo) == 0:
        raise ValueError("El grupo debe tener al menos una persona")
    
    if not all(persona["edad"] >= 18 for persona in grupo):
        raise EdadInvalidaError("Todos los asistentes deben ser mayores de edad")
    
    dnis_grupo = []
    for persona in grupo:
        dni = persona["dni"].upper()
        nombre = persona["nombre"]
        entrada = persona["entrada"]
        edad = persona["edad"]
        
        validar_dni(dni)
        validar_entrada(entrada, stock_entradas)
        validar_edad(edad)
        
        if dni in asistentes:
            raise AsistenteYaRegistradoError("El DNI ya está registrado")
        
        if dni in dnis_grupo:
            raise AsistenteYaRegistradoError("Hay DNIs repetidos en el grupo")
    
        dnis_grupo.append(dni)

    for tipo in stock_entradas:
        cantidad = 0
        for persona in grupo:
            if persona["entrada"] == tipo:
                cantidad += 1
        if cantidad > stock_entradas[tipo]:
            raise StockInsuficienteError("No hay stock suficiente de " + tipo)
        
    total = 0
    for persona in grupo:
        dni = persona["dni"].upper()
        entrada = persona["entrada"]
        nombre = persona["nombre"]
        edad = persona["edad"]

        asistentes[dni] = {
            "nombre": nombre,
            "entrada": entrada,
            "edad": edad
        }

        stock_entradas[entrada] -= 1
        total += precios_entrada[entrada]

    print("Compra realizada con éxito")
    print("Número de entradas:", len(grupo))
    print("Importe total:", total, "€")
    return total

# OPCIÓN 3: CONSULTAR ASISTENTE

def info_asistente(dni, asistentes):
    """Busca y muestra los datos de un asistente mediante su DNI."""
    if dni in asistentes:
        persona = asistentes.get(dni)
        print("Datos del asistente con DNI:", dni)
        print("Nombre:", persona.get("nombre"))
        print("Entrada:", persona.get("entrada"))
        print("Edad:", persona.get("edad"))
    else:
        raise AsistenteNoRegistradoError(
            "El DNI no está registrado"
        )


# OPCIÓN 4: CONTROL DE ACCESO

def controlar_acceso(dni, asistentes, asistentes_dentro):
    """Valida si la persona puede acceder al recinto y la marca como dentro."""
    dni = dni.upper()
    if dni not in asistentes:
        raise AsistenteNoRegistradoError("El asistente no está registrado")
    if dni in asistentes_dentro:
        raise AsistenteDentroError("El asistente ya está dentro")
    
    asistentes_dentro.add(dni)
    print("Acceso autorizado")


# FUNCIONES AUXILIARES (REGISTRO INDIVIDUAL Y VALIDACIONES)

def registrar_asistente(dni, nombre, entrada, edad, asistentes, tipo_entrada):
    """Registra manualmente a un único asistente."""
    dni = dni.upper()

    validar_dni(dni)
    validar_entrada(entrada, tipo_entrada)
    validar_edad(edad)
    if dni in asistentes:
        raise AsistenteYaRegistradoError("El asistente ya está registrado")
    
    asistentes[dni] = {
        "nombre": nombre,
        "entrada": entrada,
        "edad": edad
    }
    print("Registro realizado con éxito")

