# PYTHON – TEMA II: TIPOS DE DATOS MAPA (DICCIONARIOS)

## 1. ¿Qué es un diccionario?

Un diccionario (`dict`) permite guardar varios datos en una variable mediante parejas **clave-valor**. La clave identifica el dato y el valor contiene la información.

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])  # Ana
```

Características:
- Es mutable: podemos añadir, modificar y eliminar parejas.
- Se accede a los valores mediante claves, no mediante índices numéricos.
- Las claves deben ser únicas.
- Los valores pueden ser de cualquier tipo: números, textos, listas, tuplas u otros diccionarios.
- Las claves deben ser hashables; los ejemplos habituales son `str`, `int` y tuplas cuyos elementos también sean hashables.
- **Aclaración respecto al PDF:** en Python moderno los diccionarios conservan el orden de inserción. La afirmación del PDF de que no tienen orden está desactualizada.

## 2. Crear diccionarios

### Con llaves `{}`

```python
capitales = {
    "Francia": "París",
    "Italia": "Roma",
    "España": "Madrid"
}
print(capitales["Italia"])  # Roma
```

Cada pareja se escribe como `clave: valor`, separando las parejas con comas.

### Con el constructor `dict()`

```python
config = dict(host="localhost", port=8080, debug=True)
print(config)
```

En esta forma las claves se escriben sin comillas y deben ser identificadores válidos de Python.

### Convertir una lista de tuplas

```python
pares = [("a", 1), ("b", 2), ("c", 3)]
tabla = dict(pares)
print(tabla)  # {'a': 1, 'b': 2, 'c': 3}
```

Cada tupla aporta una pareja: el primer elemento es la clave y el segundo es el valor.

## 3. Operaciones básicas

### `len(diccionario)`

Devuelve el número de parejas clave-valor.

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(len(persona))  # 3
```

### `diccionario[clave]`

Consulta el valor asociado a una clave.

```python
producto = {"nombre": "Laptop", "precio": 1299.99}
print(producto["nombre"])  # Laptop
```

Si la clave no existe, se produce `KeyError`.

### Añadir o modificar con `diccionario[clave] = valor`

- Si la clave existe, cambia su valor.
- Si no existe, añade una pareja nueva.

```python
persona = {"nombre": "Ana", "edad": 25}
persona["edad"] = 26       # Modifica
persona["ciudad"] = "Madrid"  # Añade
print(persona)
```

## 4. Consultar con `get()`

`get()` consulta una clave sin provocar `KeyError` cuando no existe.

Sintaxis:
```python
diccionario.get(clave)
diccionario.get(clave, valor_por_defecto)
```

```python
producto = {"nombre": "Laptop", "precio": 1299.99}
print(producto.get("nombre"))                    # Laptop
print(producto.get("fabricante"))                # None
print(producto.get("fabricante", "No disponible"))  # No disponible
```

Diferencias:
- `d[clave]`: si no existe, produce `KeyError`.
- `d.get(clave)`: si no existe, devuelve `None`.
- `d.get(clave, alternativo)`: si no existe, devuelve el valor alternativo.

## 5. Añadir y actualizar: `setdefault()` y `update()`

### `setdefault(clave, valor)`

Consulta una clave y solo la añade si todavía no existe. Devuelve el valor que queda asociado a la clave.

```python
usuario = {"nombre": "Ana", "edad": 25}
print(usuario.setdefault("edad", 30))       # 25: no sustituye el valor
print(usuario.setdefault("ciudad", "Madrid"))  # Madrid: crea la clave
print(usuario)
```

### `update(otro_diccionario)`

Añade varias parejas o modifica las que ya existen.

```python
usuario = {"username": "alice_2024", "role": "analyst"}
usuario.update({"department": "Analytics", "level": 3})
usuario.update({"role": "senior_analyst"})
print(usuario)
```

También puede recibir una lista de parejas:

```python
informacion = [("proyectos", 12), ("valoracion", 4.8)]
usuario.update(informacion)
```

**Diferencia:** `setdefault()` no cambia una clave que ya existe; `update()` sí puede cambiarla.

## 6. Eliminar elementos

### `pop(clave)`

Elimina la pareja indicada y devuelve su valor.

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
eliminado = persona.pop("edad")
print(eliminado)  # 25
print(persona)
```

Si la clave no existe, produce `KeyError`, salvo que se indique un valor alternativo: `persona.pop("telefono", "No existe")`.

### `popitem()`

Elimina y devuelve la última pareja insertada, en forma de tupla `(clave, valor)`.

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
pareja = persona.popitem()
print(pareja)   # ('ciudad', 'Madrid')
print(persona)
```

### `del diccionario[clave]`

Elimina una pareja por su clave, pero no devuelve el valor.

```python
persona = {"nombre": "Ana", "edad": 25}
del persona["edad"]
print(persona)
```

Si la clave no existe, produce `KeyError`.

### `clear()`

Elimina todas las parejas y deja el diccionario vacío.

```python
persona = {"nombre": "Ana", "edad": 25}
persona.clear()
print(persona)  # {}
```

| Operación | Qué elimina | Qué devuelve |
|---|---|---|
| `pop(clave)` | La pareja indicada | El valor eliminado |
| `popitem()` | La última pareja insertada | Una tupla `(clave, valor)` |
| `del d[clave]` | La pareja indicada | Nada |
| `clear()` | Todas las parejas | Nada |

## 7. Pertenencia: `in` y `not in`

En un diccionario comprueban si una **clave** existe, no si existe un valor.

```python
persona = {"nombre": "Ana", "edad": 25}
print("nombre" in persona)  # True
print("Ana" in persona)     # False: Ana es un valor, no una clave
print("ciudad" not in persona)  # True
```

## 8. Copiar: `copy()`

`copy()` crea una copia superficial del diccionario.

```python
a = {"uno": 1, "dos": 2}
b = a.copy()
a["uno"] = 1000
print(a)  # {'uno': 1000, 'dos': 2}
print(b)  # {'uno': 1, 'dos': 2}
```

`b = a` no crea una copia: ambas variables apuntan al mismo diccionario. En cambio, `a.copy()` crea otro diccionario.

**Importante:** la copia es superficial. Si hay listas u otros diccionarios dentro, esos objetos internos pueden seguir compartiéndose. Para copiar también los objetos anidados se puede utilizar `deepcopy()`:

```python
from copy import deepcopy

original = {"notas": [7, 8, 9]}
copia = deepcopy(original)
copia["notas"].append(10)
print(original)  # {'notas': [7, 8, 9]}
print(copia)     # {'notas': [7, 8, 9, 10]}
```

## 9. Recorrer diccionarios: `keys()`, `values()` e `items()`

Un `for` directamente sobre el diccionario recorre sus claves.

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave in persona:
    print(clave)
```

### `keys()`: claves

Devuelve una vista con las claves.

```python
print(persona.keys())
for clave in persona.keys():
    print(clave)
```

### `values()`: valores

Devuelve una vista con los valores.

```python
print(persona.values())
for valor in persona.values():
    print(valor)
```

### `items()`: parejas clave-valor

Devuelve una vista de parejas. Cada pareja se puede tratar como una tupla de dos elementos.

```python
print(persona.items())

for clave, valor in persona.items():
    print(clave, ":", valor)
```

| Método | Devuelve |
|---|---|
| `keys()` | Las claves |
| `values()` | Los valores |
| `items()` | Las parejas clave-valor |

Estos métodos devuelven **vistas** (`dict_keys`, `dict_values`, `dict_items`), no listas normales. Reflejan los cambios que se hagan posteriormente en el diccionario.

```python
datos = {"a": 1, "b": 2}
claves = datos.keys()
print(claves)  # dict_keys(['a', 'b'])
datos["c"] = 3
print(claves)  # dict_keys(['a', 'b', 'c'])
```

## 10. Operaciones de conjuntos sobre las claves

Las vistas de claves permiten comparar las claves de dos diccionarios:

- `&`: intersección, claves comunes.
- `|`: unión, todas las claves sin repetir.
- `-`: diferencia, claves que están en el primero pero no en el segundo.
- `^`: diferencia simétrica, claves que están en uno u otro, pero no en ambos.

```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

print(dict1.keys() & dict2.keys())  # {'b', 'c'}
print(dict1.keys() | dict2.keys())  # {'a', 'b', 'c', 'd'}
print(dict1.keys() - dict2.keys())  # {'a'}
print(dict1.keys() ^ dict2.keys())  # {'a', 'd'}
```

Estas operaciones comparan las claves, no los valores.

## 11. Claves y valores de distintos tipos

Las claves no tienen por qué ser siempre cadenas. Se pueden usar números y tuplas válidas como claves. No se pueden usar listas ni diccionarios como claves porque son mutables y no son hashables.

Los valores sí pueden ser de distintos tipos.

```python
datos = {
    "nombre": "Ana",
    10: "diez",
    3.5: "decimal",
    (1, 2): "tupla"
}

print(datos["nombre"])
print(datos[10])
print(datos[(1, 2)])
```

## 12. Diccionarios anidados

Los valores pueden ser listas, tuplas u otros diccionarios.

### Diccionario con listas

```python
alumnos = {
    "Ana": [7, 8, 9],
    "Luis": [6, 5, 8]
}

print(alumnos["Ana"])     # [7, 8, 9]
print(alumnos["Ana"][0])  # 7
```

`alumnos["Ana"]` obtiene la lista y `[0]` accede al primer elemento de esa lista.

### Diccionario dentro de otro diccionario

```python
alumnos = {
    "alumno1": {"nombre": "Ana", "edad": 20},
    "alumno2": {"nombre": "Luis", "edad": 22}
}

print(alumnos["alumno1"]["nombre"])  # Ana
print(alumnos["alumno2"]["edad"])    # 22
```

Primero se accede al diccionario interior mediante la clave exterior y después al dato mediante su clave interior.

## 13. `fromkeys()`

El PDF lo incluye en la lista de métodos principales, aunque no desarrolla su explicación.

`fromkeys()` crea un diccionario a partir de una colección de claves y asigna a todas el mismo valor inicial.

**Sintaxis:**

```python
dict.fromkeys(secuencia_de_claves, valor)
```

```python
claves = ["nombre", "edad", "ciudad"]
datos = dict.fromkeys(claves, "Sin indicar")
print(datos)
# {'nombre': 'Sin indicar', 'edad': 'Sin indicar', 'ciudad': 'Sin indicar'}
```

El valor es opcional. Si no se indica, se utiliza `None`.

## 14. Tabla general de métodos

| Método | Descripción |
|---|---|
| `clear()` | Elimina todos los elementos. |
| `copy()` | Crea una copia superficial. |
| `fromkeys()` | Crea un diccionario con unas claves y un mismo valor inicial. |
| `get()` | Consulta una clave sin provocar `KeyError` si no existe. |
| `items()` | Devuelve una vista de las parejas clave-valor. |
| `keys()` | Devuelve una vista de las claves. |
| `pop()` | Elimina una clave y devuelve su valor. |
| `popitem()` | Elimina y devuelve la última pareja insertada. |
| `setdefault()` | Añade una clave solo si no existe. |
| `update()` | Añade o modifica varias parejas. |
| `values()` | Devuelve una vista de los valores. |

## 15. Trampas habituales de examen

1. `in` comprueba claves, no valores.
2. `d[clave]` produce `KeyError` si la clave no existe; `get()` no.
3. `setdefault()` no sustituye el valor de una clave existente; `update()` sí puede hacerlo.
4. `pop(clave)` elimina por clave; `popitem()` elimina la última pareja insertada.
5. `del` elimina, pero no devuelve el valor; `pop()` sí.
6. `copy()` es una copia superficial, no profunda.
7. `keys()`, `values()` e `items()` devuelven vistas distintas.
8. Las claves pueden ser cadenas, números o tuplas válidas; no listas ni diccionarios.
9. Los valores pueden ser de diferentes tipos y contener estructuras anidadas.
10. Las claves son únicas: asignar de nuevo una clave existente sustituye su valor.

## 16. Qué debes dominar

- Crear diccionarios con `{}` y `dict()`.
- Distinguir clave y valor.
- Consultar, modificar y añadir parejas.
- Saber cuándo utilizar `get()`.
- Diferenciar `setdefault()` y `update()`.
- Eliminar con `pop()`, `popitem()`, `del` y `clear()`.
- Comprobar claves con `in` y `not in`.
- Copiar con `copy()`.
- Recorrer claves, valores y parejas con `keys()`, `values()` e `items()`.
- Realizar operaciones de conjuntos sobre las vistas de claves.
- Acceder a listas y diccionarios anidados.
