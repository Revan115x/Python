# PYTHON – CHULETA DE MÉTODOS, FUNCIONES Y PARÁMETROS

## 1. DIFERENCIA ENTRE FUNCIÓN Y MÉTODO

En Python podemos utilizar funciones y métodos.

**Función:** se escribe directamente y puede recibir parámetros.

```python
len("Hola")
```

**Método:** pertenece a un objeto y se escribe utilizando un punto.

```python
texto.isdigit()
```

- `len()` es una función.
- `.isdigit()` es un método de las cadenas de texto.

---

# 2. MÉTODOS DE CADENAS DE TEXTO (STRING)

Son métodos que permiten comprobar, modificar o buscar información dentro de un texto.

Supongamos:

```python
texto = "Hola Mundo 123"
```

## 2.1. Métodos para comprobar caracteres

### isdigit()

Comprueba si todos los caracteres de una cadena son dígitos.

**Sintaxis:**

```python
cadena.isdigit()
```

**Parámetros:** ninguno.

**Devuelve:** `True` o `False`.

```python
numero = "12345"

print(numero.isdigit())
```

Resultado:

```text
True
```

Otro ejemplo:

```python
numero = "12A45"

print(numero.isdigit())
```

Resultado:

```text
False
```

### isalpha()

Comprueba si todos los caracteres son letras.

```python
texto = "Hola"

print(texto.isalpha())
```

Resultado: `True`

```python
texto = "Hola123"

print(texto.isalpha())
```

Resultado: `False`

### isalnum()

Comprueba si todos los caracteres son letras o números.

```python
texto = "Hola123"

print(texto.isalnum())
```

Resultado: `True`

Si contiene espacios o símbolos, devuelve `False`.

### isspace()

Comprueba si una cadena contiene únicamente espacios en blanco.

```python
texto = "   "

print(texto.isspace())
```

Resultado: `True`

### isupper()

Comprueba si las letras están en mayúsculas.

```python
texto = "HOLA"

print(texto.isupper())
```

Resultado: `True`

### islower()

Comprueba si las letras están en minúsculas.

```python
texto = "hola"

print(texto.islower())
```

Resultado: `True`

## 2.2. Métodos para modificar textos

### upper()

Convierte el texto a mayúsculas.

```python
texto = "hola mundo"

print(texto.upper())
```

Resultado: `HOLA MUNDO`

### lower()

Convierte el texto a minúsculas.

```python
texto = "HOLA MUNDO"

print(texto.lower())
```

Resultado: `hola mundo`

### capitalize()

Pone la primera letra en mayúscula y el resto en minúsculas.

```python
texto = "hOLA mUNDO"

print(texto.capitalize())
```

Resultado: `Hola mundo`

### title()

Pone la primera letra de cada palabra en mayúscula.

```python
texto = "hola mundo"

print(texto.title())
```

Resultado: `Hola Mundo`

### strip()

Elimina los espacios en blanco del principio y del final.

```python
texto = "   Hola   "

print(texto.strip())
```

Resultado: `Hola`

También existen:

- `lstrip()`: elimina espacios de la izquierda.
- `rstrip()`: elimina espacios de la derecha.

### replace()

Reemplaza una parte del texto por otra.

**Parámetros:**
- `old`: texto que queremos sustituir.
- `new`: texto nuevo.
- `count`: número máximo de sustituciones (opcional).

```python
texto = "Hola Juan"

print(texto.replace("Juan", "Pedro"))
```

Resultado: `Hola Pedro`

Ejemplo con el tercer parámetro:

```python
texto = "Hola Hola Hola"

print(texto.replace("Hola", "Adios", 1))
```

Resultado: `Adios Hola Hola`

## 2.3. Métodos para buscar información

### find()

Busca una palabra o carácter y devuelve su posición.

**Parámetros:**
- `sub`: texto que queremos buscar.
- `start`: posición inicial (opcional).
- `end`: posición final (opcional).

```python
texto = "Hola Mundo"

print(texto.find("Mundo"))
```

Resultado: `5`

Si no encuentra el texto devuelve `-1`.

### count()

Cuenta cuántas veces aparece un carácter o una palabra.

**Parámetros:**
- `sub`: elemento que queremos contar.
- `start`: posición inicial (opcional).
- `end`: posición final (opcional).

```python
texto = "Hola Hola Hola"

print(texto.count("Hola"))
```

Resultado: `3`

### startswith()

Comprueba si el texto comienza por una cadena determinada.

```python
texto = "Python es fácil"

print(texto.startswith("Python"))
```

Resultado: `True`

### endswith()

Comprueba si el texto termina por una cadena determinada.

```python
texto = "archivo.pdf"

print(texto.endswith(".pdf"))
```

Resultado: `True`

---

# 3. FUNCIONES GENERALES DE PYTHON

Estas funciones pueden utilizarse con diferentes tipos de datos.

## len()

Devuelve la longitud de una cadena, lista o tupla.

```python
texto = "Python"

print(len(texto))
```

Resultado: `6`

## max()

Devuelve el elemento de mayor valor.

```python
numeros = [5, 8, 2, 10, 4]

print(max(numeros))
```

Resultado: `10`

## min()

Devuelve el elemento de menor valor.

```python
numeros = [5, 8, 2, 10, 4]

print(min(numeros))
```

Resultado: `2`

## sum()

Suma los elementos numéricos de una colección.

```python
numeros = [5, 8, 2, 10]

print(sum(numeros))
```

Resultado: `25`

## sorted()

Devuelve una nueva lista con los elementos ordenados.

**Parámetros:**
- `iterable`: colección que queremos ordenar.
- `reverse`: si es `True`, ordena de mayor a menor (opcional).
- `key`: criterio de ordenación (opcional).

```python
numeros = [5, 2, 8, 1]

print(sorted(numeros))
```

Resultado: `[1, 2, 5, 8]`

De mayor a menor:

```python
print(sorted(numeros, reverse=True))
```

Resultado: `[8, 5, 2, 1]`

## type()

Indica el tipo de dato de una variable.

```python
numero = 10

print(type(numero))
```

Resultado: `<class 'int'>`

## range()

Genera una secuencia de números.

**Parámetros:**
- `start`: número inicial (opcional).
- `stop`: número final, que no se incluye.
- `step`: incremento entre números (opcional).

```python
for i in range(5):
    print(i)
```

Resultado: `0, 1, 2, 3, 4`

Con inicio y final:

```python
for i in range(1, 6):
    print(i)
```

Resultado: `1, 2, 3, 4, 5`

Con salto:

```python
for i in range(0, 10, 2):
    print(i)
```

Resultado: `0, 2, 4, 6, 8`

---

# 4. MÉTODOS DE LISTAS

Supongamos:

```python
numeros = [5, 10, 15, 20]
```

## append()

Añade un elemento al final de la lista.

**Parámetro:** elemento que queremos añadir.

```python
numeros.append(25)

print(numeros)
```

Resultado: `[5, 10, 15, 20, 25]`

## insert()

Inserta un elemento en una posición determinada.

**Parámetros:**
- `index`: posición donde insertar.
- `element`: elemento que queremos añadir.

```python
numeros.insert(0, 100)
```

Resultado: `[100, 5, 10, 15, 20]`

## remove()

Elimina la primera aparición de un elemento.

**Parámetro:** elemento que queremos eliminar.

```python
numeros.remove(10)
```

Resultado: `[5, 15, 20]`

## pop()

Elimina un elemento y lo devuelve.

**Parámetro:** índice del elemento (opcional). Si no se indica, elimina el último.

```python
numeros.pop()
```

Elimina el último elemento.

```python
numeros.pop(0)
```

Elimina el elemento de la posición 0.

## sort()

Ordena la lista original.

**Parámetros:**
- `reverse`: orden inverso si es `True` (opcional).
- `key`: criterio de ordenación (opcional).

```python
numeros.sort()
```

Ordena de menor a mayor.

```python
numeros.sort(reverse=True)
```

Ordena de mayor a menor.

## reverse()

Invierte el orden de los elementos de la lista.

```python
numeros.reverse()
```

## index()

Devuelve la posición de la primera aparición de un elemento.

**Parámetros:**
- `element`: elemento buscado.
- `start`: posición inicial (opcional).
- `end`: posición final (opcional).

```python
numeros = [10, 20, 30]

print(numeros.index(20))
```

Resultado: `1`

## clear()

Elimina todos los elementos.

```python
numeros.clear()
```

Resultado: `[]`

## copy()

Crea una copia superficial de la lista.

```python
numeros = [1, 2, 3]

copia = numeros.copy()
```

---

# 5. CONVERSIONES DE TIPOS

Estas funciones permiten convertir datos de un tipo a otro.

| Función | Utilidad | Ejemplo |
|---|---|---|
| `int()` | Convierte a entero | `int("25")` |
| `float()` | Convierte a decimal | `float("2.5")` |
| `str()` | Convierte a texto | `str(25)` |
| `bool()` | Convierte a booleano | `bool(1)` |
| `list()` | Convierte a lista | `list("Hola")` |
| `tuple()` | Convierte a tupla | `tuple([1,2])` |

Ejemplo:

```python
edad = input("Introduce tu edad: ")

edad = int(edad)

print(edad + 1)
```

IMPORTANTE: `input()` siempre devuelve una cadena de texto. Si queremos realizar operaciones matemáticas debemos convertirla.

---

# 6. FUNCIONES PARA TRABAJAR CON TEXTO Y NÚMEROS

## input()

Permite introducir información por teclado.

**Parámetro:** mensaje que queremos mostrar (opcional).

```python
nombre = input("Introduce tu nombre: ")
```

## print()

Muestra información por pantalla.

Parámetros habituales:

- `*objects`: elementos que queremos mostrar.
- `sep`: separador entre elementos.
- `end`: carácter final (por defecto es un salto de línea).

```python
print("Hola", "Juan", sep="-")
```

Resultado: `Hola-Juan`

```python
print("Hola", end=" ")
print("Juan")
```

Resultado: `Hola Juan`

## abs()

Devuelve el valor absoluto de un número.

```python
print(abs(-10))
```

Resultado: `10`

## round()

Redondea un número.

**Parámetros:**
- `number`: número que queremos redondear.
- `ndigits`: número de decimales (opcional).

```python
print(round(3.14159, 2))
```

Resultado: `3.14`

---

# 7. MÉTODOS Y FUNCIONES DEL MÓDULO RANDOM

Primero debemos importar el módulo:

```python
import random
```

## random.randint()

Genera un número entero aleatorio entre dos valores, incluyendo ambos extremos.

**Parámetros:**
- `a`: número mínimo.
- `b`: número máximo.

```python
numero = random.randint(1, 10)

print(numero)
```

## random.randrange()

Genera un número de una secuencia.

**Parámetros:**
- `start`: inicio.
- `stop`: final (no incluido).
- `step`: salto (opcional).

```python
numero = random.randrange(1, 10)
```

## random.choice()

Selecciona un elemento aleatorio de una secuencia.

**Parámetro:** secuencia de elementos.

```python
numeros = [1, 2, 3, 4, 5]

print(random.choice(numeros))
```

---

# 8. OPERACIONES IMPORTANTES CON LISTAS Y CADENAS

## in

Comprueba si un elemento existe dentro de una colección o cadena.

```python
numeros = [1, 2, 3, 4]

print(3 in numeros)
```

Resultado: `True`

## not in

Comprueba si un elemento NO existe.

```python
print(8 not in numeros)
```

Resultado: `True`

## Concatenar cadenas

Une dos cadenas.

```python
nombre = "Jose"
apellido = "Arriaga"

nombreCompleto = nombre + " " + apellido
```

## Repetir cadenas

```python
texto = "Hola " * 3

print(texto)
```

Resultado: `Hola Hola Hola`

## Acceder a posiciones

```python
texto = "Python"

print(texto[0])
```

Resultado: `P`

Las posiciones comienzan en 0.

---

# 9. TABLA RÁPIDA PARA EL EXAMEN

| Quiero... | Utilizo |
|---|---|
| Saber si una cadena contiene números | `.isdigit()` |
| Saber si contiene letras | `.isalpha()` |
| Saber si contiene letras y números | `.isalnum()` |
| Comprobar si son espacios | `.isspace()` |
| Pasar a mayúsculas | `.upper()` |
| Pasar a minúsculas | `.lower()` |
| Eliminar espacios exteriores | `.strip()` |
| Sustituir caracteres | `.replace()` |
| Buscar una palabra | `.find()` |
| Contar apariciones | `.count()` |
| Saber si empieza por algo | `.startswith()` |
| Saber si termina por algo | `.endswith()` |
| Conocer la longitud | `len()` |
| Obtener el máximo | `max()` |
| Obtener el mínimo | `min()` |
| Sumar elementos | `sum()` |
| Ordenar una lista | `.sort()` |
| Añadir a una lista | `.append()` |
| Insertar en una posición | `.insert()` |
| Eliminar un elemento | `.remove()` |
| Eliminar por posición | `.pop()` |
| Obtener la posición | `.index()` |
| Comprobar si existe | `in` |
| Generar números aleatorios | `random.randint()` |
| Convertir a entero | `int()` |
| Convertir a decimal | `float()` |
| Convertir a texto | `str()` |

---

# 10. ERRORES HABITUALES EN EL EXAMEN

1. Confundir `isdigit()` con `int()`: el primero comprueba si hay dígitos; el segundo convierte un valor a entero cuando es posible.
2. Pensar que `range(1, 10)` incluye el 10: NO, termina en 9.
3. Confundir `append()` con `insert()`: append añade al final; insert permite indicar una posición.
4. Confundir `remove()` con `pop()`: remove elimina por valor; pop elimina por posición.
5. Pensar que `sort()` devuelve una lista nueva: modifica la lista original y devuelve `None`.
6. Olvidar que `input()` devuelve texto.
7. Confundir `find()` con `count()`: find busca la posición; count cuenta las apariciones.
8. Olvidar que `replace()` devuelve una cadena modificada, pero no cambia automáticamente la variable original.
9. Pensar que `isdigit()` admite espacios: `"123 "` devuelve `False`.
10. Olvidar que los índices empiezan en 0.

**RECUERDA:** Los métodos que terminan en `()` se ejecutan utilizando paréntesis. Algunos necesitan parámetros y otros no. No debes inventar parámetros: consulta siempre qué admite cada método.