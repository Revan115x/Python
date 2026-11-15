# PYTHON – TEMA 3: TIPOS DE DATOS SECUENCIA

# 1. TIPOS DE DATOS SECUENCIA (CONTENEDORES)

Los tipos de datos secuencia permiten **guardar varios datos dentro de una misma variable**.

Por ejemplo, en lugar de crear cinco variables para guardar cinco nombres, podemos utilizar una lista.

Python dispone de los siguientes tipos:

| Tipo | ¿Para qué sirve? | ¿Se puede modificar? |
|---|---|---|
| `list` | Guardar varios elementos, incluso repetidos. | Sí (mutable) |
| `tuple` | Guardar varios elementos sin modificarlos. | No (inmutable) |
| `range` | Crear secuencias de números. | No (inmutable) |
| `set` | Guardar elementos sin repeticiones y sin orden fijo. | Sí (mutable) |
| `frozenset` | Igual que un conjunto, pero sin posibilidad de modificarlo. | No (inmutable) |

**Conceptos importantes:**

- Mutable: significa que podemos modificar el contenido después de crearlo.
- Inmutable: significa que no podemos modificar el contenido después de crearlo.
- Ordenado: mantiene una posición para cada elemento.
- Duplicados: elementos que aparecen más de una vez.

---

# 2. LISTAS (list)

## 2.1. ¿Qué es una lista?

Una lista es una colección de elementos que permite guardar varios datos dentro de una variable.

Características:

- Tienen orden: cada elemento tiene una posición.
- Pueden contener diferentes tipos de datos.
- Permiten elementos repetidos.
- Son mutables: podemos añadir, eliminar y modificar elementos.

**Sintaxis:**

```python
lista = [elemento1, elemento2, elemento3]
```

**Ejemplo:**

```python
datos = [1, "dos", [3, 4], True]

print(datos)
```

Resultado:

```text
[1, 'dos', [3, 4], True]
```

Podemos guardar números, cadenas, otras listas y valores booleanos dentro de una misma lista.

## 2.2. Acceder a los elementos: indexación

Cada elemento tiene una posición llamada índice.

¡IMPORTANTE! En Python los índices empiezan por 0.

Ejemplo:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[0])  # 10
print(numeros[1])  # 20
print(numeros[2])  # 30
```

También podemos utilizar índices negativos para empezar a contar desde el final.

| Índice | Elemento |
|---|---|
| `0` | 10 |
| `1` | 20 |
| `2` | 30 |
| `3` | 40 |
| `4` | 50 |
| `-1` | 50 |
| `-2` | 40 |
| `-3` | 30 |

Ejemplo:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[-1])  # 50
print(numeros[-2])  # 40
```

**Truco para el examen:** El índice `0` es el primer elemento y `-1` es el último.

## 2.3. Sublistas o segmentación (slicing)

Permite obtener una parte de una lista.

**Sintaxis:**

```python
lista[inicio:final:salto]
```

- `inicio`: posición donde empezamos.
- `final`: posición donde terminamos (NO se incluye).
- `salto`: cada cuántos elementos avanzamos.

Ejemplo:

```python
a = ['P', 'y', 't', 'h', 'o', 'n']

print(a[1:4])
```

Resultado:

```text
['y', 't', 'h']
```

¿Por qué? Empieza en el índice 1 y llega hasta el índice 3. El índice 4 no se incluye.

**Más ejemplos:**

```python
a = ['P', 'y', 't', 'h', 'o', 'n']

print(a[1:1])   # []
print(a[:-3])   # ['P', 'y', 't']
print(a[:])     # Toda la lista
print(a[0:6:2]) # ['P', 't', 'o']
```

Explicación:

| Expresión | Qué hace |
|---|---|
| `a[1:4]` | Desde el índice 1 hasta antes del 4. |
| `a[1:1]` | No devuelve elementos. |
| `a[:-3]` | Desde el principio hasta antes de los últimos 3 elementos. |
| `a[:]` | Copia todos los elementos en una nueva lista. |
| `a[0:6:2]` | Empieza en 0 y avanza de 2 en 2. |

**Truco:** El límite final nunca se incluye.

## 2.4. Crear listas con list()

También podemos crear listas utilizando la función `list()`.

**Sintaxis:**

```python
list()
```

Crea una lista a partir de una secuencia o colección.

Ejemplos:

```python
lista1 = list()

print(lista1)
```

Resultado:

```text
[]
```

También podemos convertir una cadena en una lista:

```python
lista2 = list("Python")

print(lista2)
```

Resultado:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

Cada carácter de la cadena se convierte en un elemento independiente.

## 2.5. Convertir una lista de cadenas en una cadena: join()

El método `join()` permite unir los elementos de una lista de cadenas utilizando un separador.

**Sintaxis:**

```python
separador.join(lista)
```

Ejemplo:

```python
palabras = ["Hola", "que", "tal"]

resultado = " ".join(palabras)

print(resultado)
```

Resultado:

```text
Hola que tal
```

Otro ejemplo:

```python
palabras = ["Python", "Java", "C#"]

resultado = "-".join(palabras)

print(resultado)
```

Resultado:

```text
Python-Java-C#
```

**Importante:**

- `" ".join(lista)` separa los elementos con espacios.
- `"-".join(lista)` separa los elementos con guiones.
- `"".join(lista)` los une sin separadores.

Recuerda que `join()` espera una secuencia de cadenas, no una lista de números.

---

# 3. OPERACIONES CON LISTAS

Podemos dividir las operaciones en dos grupos:

1. Operaciones que NO modifican la lista original.
2. Operaciones que SÍ modifican la lista original.

## 3.1. Operaciones que NO modifican una lista

### len(lista)

Devuelve el número de elementos que tiene una lista.

```python
numeros = [10, 20, 30, 40]

print(len(numeros))
```

Resultado:

```text
4
```

### min(lista)

Devuelve el elemento más pequeño.

```python
numeros = [8, 3, 10, 2]

print(min(numeros))
```

Resultado:

```text
2
```

### max(lista)

Devuelve el elemento más grande.

```python
numeros = [8, 3, 10, 2]

print(max(numeros))
```

Resultado:

```text
10
```

### sum(lista)

Suma todos los elementos de una lista de números.

```python
numeros = [10, 20, 30]

print(sum(numeros))
```

Resultado:

```text
60
```

### dato in lista

Comprueba si un elemento existe dentro de una lista.

Devuelve `True` o `False`.

```python
numeros = [10, 20, 30]

print(20 in numeros)  # True
print(50 in numeros)  # False
```

### lista.index(dato)

Devuelve la posición del primer elemento que coincide con el valor buscado.

```python
numeros = [10, 20, 30, 20]

print(numeros.index(20))
```

Resultado:

```text
1
```

¡Cuidado! Aunque el número 20 aparece dos veces, devuelve la posición de la primera aparición.

### lista.count(dato)

Cuenta cuántas veces aparece un elemento.

```python
numeros = [10, 20, 30, 20, 20]

print(numeros.count(20))
```

Resultado:

```text
3
```

### all(lista)

Devuelve `True` si todos los elementos son verdaderos.

```python
numeros = [1, 2, 3]

print(all(numeros))
```

Resultado:

```text
True
```

Si existe algún elemento considerado falso, devuelve `False`.

```python
numeros = [1, 0, 3]

print(all(numeros))
```

Resultado:

```text
False
```

### any(lista)

Devuelve `True` si al menos un elemento es verdadero.

```python
numeros = [0, 0, 3]

print(any(numeros))
```

Resultado:

```text
True
```

Si todos los elementos son falsos, devuelve `False`.

```python
numeros = [0, False, 0]

print(any(numeros))
```

Resultado:

```text
False
```

**IMPORTANTE: ¿Qué considera Python verdadero o falso?**

- `0` → False.
- `False` → False.
- `""` → False.
- `[]` → False.
- Los números distintos de 0 → True.
- Las cadenas no vacías → True.
- Las listas no vacías → True.

### Tabla de repaso

| Función / operación | ¿Qué hace? |
|---|---|
| `len(l)` | Cuenta elementos. |
| `min(l)` | Devuelve el mínimo. |
| `max(l)` | Devuelve el máximo. |
| `sum(l)` | Suma los elementos. |
| `dato in l` | Comprueba si existe. |
| `l.index(dato)` | Busca la posición de la primera aparición. |
| `l.count(dato)` | Cuenta las apariciones. |
| `all(l)` | Comprueba si todos son verdaderos. |
| `any(l)` | Comprueba si alguno es verdadero. |

## 3.2. Operaciones que SÍ modifican una lista

### lista1 + lista2

Concatena dos listas y crea una nueva lista.

```python
a = [1, 2]
b = [3, 4]

c = a + b

print(c)
```

Resultado:

```text
[1, 2, 3, 4]
```

No modifica las listas originales.

### append(dato)

Añade un elemento al final de la lista.

**Sintaxis:**

```python
lista.append(dato)
```

Ejemplo:

```python
numeros = [1, 2, 3]

numeros.append(4)

print(numeros)
```

Resultado:

```text
[1, 2, 3, 4]
```

### extend(secuencia)

Añade varios elementos al final de una lista.

**Sintaxis:**

```python
lista.extend(secuencia)
```

Ejemplo:

```python
numeros = [1, 2, 3]

numeros.extend([4, 5, 6])

print(numeros)
```

Resultado:

```text
[1, 2, 3, 4, 5, 6]
```

### insert(índice, dato)

Inserta un elemento en una posición determinada.

**Sintaxis:**

```python
lista.insert(indice, dato)
```

Ejemplo:

```python
numeros = [10, 20, 40]

numeros.insert(2, 30)

print(numeros)
```

Resultado:

```text
[10, 20, 30, 40]
```

El número 30 se introduce en el índice 2 y los demás elementos se desplazan.

### remove(dato)

Elimina la primera aparición de un elemento por su valor.

**Sintaxis:**

```python
lista.remove(dato)
```

Ejemplo:

```python
numeros = [10, 20, 30, 20]

numeros.remove(20)

print(numeros)
```

Resultado:

```text
[10, 30, 20]
```

¡Cuidado! Elimina solamente la primera aparición.

Si el elemento no existe, produce un error.

### pop([índice])

Elimina un elemento y además lo devuelve.

**Sintaxis:**

```python
lista.pop()
lista.pop(indice)
```

Ejemplo 1: eliminar el último elemento.

```python
numeros = [10, 20, 30]

resultado = numeros.pop()

print(resultado)
print(numeros)
```

Resultado