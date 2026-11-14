# Fundamentos del lenguaje Python

**Asignatura:** Programación – DAW  
**Material principal:** *1. Fundamentos del lenguaje.pdf*  
**Nivel:** iniciación

## Índice
1. Introducción a Python
2. Generalidades y reglas de escritura
3. Ayuda en Python
4. Literales
5. Variables y constantes
6. Tipos de datos y conversiones
7. Operadores
8. Objetos mutables e inmutables
9. Entrada y salida estándar
10. Funciones predefinidas
11. Chuleta final
12. Aclaraciones sobre el PDF

---

## 1. Introducción a Python

Python es un lenguaje de programación que permite escribir instrucciones para que un ordenador realice tareas. El material destaca estas características:

- **Fácil de aprender y leer:** su sintaxis suele ser sencilla y compacta.
- **Interpretado:** el código se ejecuta mediante el intérprete de Python. Normalmente no tenemos que compilar y enlazar manualmente el programa.
- **Tipado dinámico:** no hace falta declarar previamente el tipo de una variable. El tipo depende del valor asignado y puede cambiar al asignarle otro.
- **Orientado a objetos:** permite organizar programas mediante objetos y clases.
- **Modular:** podemos dividir un programa en módulos y reutilizar código.
- **Biblioteca estándar:** incluye módulos para trabajar con archivos, sistema, comunicaciones y otras tareas.

Ejemplo:

```python
nombre = "Ana"
edad = 20

print("Hola", nombre)
print("Tienes", edad, "años")
```

Resultado:
```text
Hola Ana
Tienes 20 años
```

## 2. Generalidades y reglas de escritura

Un programa Python está formado por instrucciones. Normalmente, cada instrucción termina al llegar al salto de línea.

### 2.1. Salto de línea y punto y coma

```python
nombre = "Ana"
edad = 20
```

También se pueden separar varias instrucciones con `;`, aunque no se recomienda porque hace el código menos legible:

```python
nombre = "Ana"; edad = 20
```

**Recomendación:** una instrucción por línea.

### 2.2. Indentación o sangría

La **indentación** son los espacios al principio de una línea que indican que pertenece a un bloque:

```python
edad = 20

if edad >= 18:
    print("Es mayor de edad")
    print("Puede acceder")
```

Las dos instrucciones indentadas pertenecen al bloque del `if`.

- Se recomienda utilizar **4 espacios**.
- Se pueden utilizar espacios o tabulaciones, pero no se deben mezclar.
- Una indentación incorrecta puede provocar un `IndentationError`.

### 2.3. Dividir instrucciones largas

Una barra invertida `\` al final de una línea permite continuar la instrucción en la siguiente:

```python
resultado = 10 + 20 + \
            30 + 40
```

También se pueden escribir expresiones en varias líneas dentro de paréntesis, corchetes o llaves:

```python
resultado = (
    10 + 20
    + 30 + 40
)
```

### 2.4. Bloques de una sola línea

Si el bloque ocupa una sola instrucción, puede escribirse después de los dos puntos:

```python
if edad >= 18: print("Mayor de edad")
```

Aunque es válido, para aprender y mantener el código claro es preferible utilizar una línea nueva con indentación.

### 2.5. Comentarios

Un comentario sirve para explicar el código. Python ignora los comentarios que empiezan por `#`.

```python
# Guardamos el nombre del usuario
nombre = "Ana"
```

Para un comentario de varias líneas podemos poner `#` en cada línea:

```python
# Este programa guarda
# un nombre y lo muestra
nombre = "Ana"
```

También se pueden escribir cadenas con triple comilla, simple o doble. **Importante:** no son comentarios propiamente dichos; son cadenas de texto. Se utilizan, entre otros usos, para documentar módulos, clases y funciones (*docstrings*), pero no son ignoradas como los comentarios `#`.

## 3. Ayuda en Python

La función `help()` permite consultar la documentación de Python desde una sesión interactiva.

### Ayuda general

```python
help()
```

Abre el sistema de ayuda interactivo. Para salir normalmente se escribe `quit`.

### Ayuda de un elemento concreto

```python
help(print)
help(input)
help(str)
```

Entre paréntesis indicamos el elemento del que queremos información. Es especialmente útil en el intérprete interactivo.

## 4. Literales

Un **literal** es una forma de escribir directamente un valor en el código.

### 4.1. Literales numéricos

**Enteros (`int`):** números sin parte decimal.

```python
cantidad = 12
temperatura = -23
```

También podemos escribir enteros en otras bases:

| Base | Prefijo | Ejemplo |
|---|---|---|
| Binaria | `0b` | `0b10101` |
| Octal | `0o` | `0o377` |
| Hexadecimal | `0x` | `0xff` |

**Reales (`float`):** utilizan un punto para separar la parte entera de la decimal.

```python
precio = 12.3
otro = 10.
pequeno = .001
```

Para números muy grandes o pequeños se puede usar notación exponencial:

```python
numero_pequeno = 3.14e-10
numero_grande = 1e100
```

`3.14e-10` significa `3.14 × 10⁻¹⁰`.

**Complejos (`complex`):** tienen una parte real y otra imaginaria. Python utiliza `j` para la parte imaginaria:

```python
numero = 1 + 2j
```

### 4.2. Literales de cadena (`str`)

Representan texto y se escriben entre comillas simples o dobles:

```python
nombre = 'Lucía'
saludo = "Hola"
```

Las secuencias de escape permiten representar caracteres especiales:

| Secuencia | Significado |
|---|---|
| `\\` | Barra invertida `\` |
| `\'` | Comilla simple |
| `\"` | Comilla doble |
| `\n` | Salto de línea |
| `\t` | Tabulación horizontal |
| `\r` | Retorno de carro |
| `\b` | Retroceso |
| `\a` | Señal de alerta |
| `\f` | Salto de página |
| `\v` | Tabulación vertical |

Ejemplo:

```python
texto = "Primera línea\nSegunda línea"
print(texto)
```

Resultado:
```text
Primera línea
Segunda línea
```

## 5. Variables y constantes

### 5.1. Variables

Una **variable** es un nombre que utilizamos para referirnos a un valor u objeto. En Python no es necesario declararla antes de usarla:

```python
edad = 20
nombre = "Lucía"
```

Reglas para nombrarlas:

- Deben empezar por una letra o por `_`.
- Después pueden contener letras, números y guiones bajos.
- No pueden empezar por un número.
- Python distingue mayúsculas y minúsculas: `edad` y `Edad` son nombres distintos.
- Se recomienda utilizar nombres descriptivos y, normalmente, minúsculas.

Válidos: `nombre`, `edad2`, `_contador`, `precio_total`.  
No válidos: `2edad`, `precio-total`, `mi nombre`.

### 5.2. Tipado dinámico

El tipo no queda fijado para siempre en el nombre de la variable:

```python
dato = 5
print(type(dato))  # <class 'int'>

dato = "hola"
print(type(dato))  # <class 'str'>
```

### 5.3. Borrar una variable: `del`

`del` elimina el nombre de la variable:

```python
numero = 5
del numero
```

Si intentamos utilizar `numero` después, obtendremos un `NameError` porque ese nombre ya no está definido.

### 5.4. El valor `None`

Podemos asignar `None` para indicar que una variable no contiene actualmente un valor normal:

```python
resultado = None
print(type(resultado))  # <class 'NoneType'>
```

`None` no es lo mismo que `0`, `False` o una cadena vacía.

### 5.5. Anotaciones de tipo

Las anotaciones indican el tipo esperado, pero no convierten automáticamente el valor ni impiden asignar otro tipo:

```python
edad: int = 20
precio: float = 12.5
```

### 5.6. Constantes

Python no tiene una instrucción que convierta una variable en constante de forma obligatoria. Por convención, escribimos su nombre en mayúsculas para indicar que no debería cambiar:

```python
IVA = 0.21
```

El PDF explica también la posibilidad de guardar constantes en otro módulo y acceder a ellas mediante `import`.

**constantes.py**
```python
IVA = 0.21
PI = 3.14159
```

**principal.py**
```python
import constantes

precio = 100
total = precio + precio * constantes.IVA

print(total)
```

Resultado:
```text
121.0
```

`constantes.IVA` accede al nombre `IVA` que está dentro del módulo `constantes`.

## 6. Tipos de datos y conversiones

El tipo de un dato determina qué clase de valor representa y qué operaciones podemos realizar con él.

### 6.1. Tipos que enumera el material

| Grupo | Tipo | Qué representa |
|---|---|---|
| Numérico | `int` | Números enteros |
| Numérico | `float` | Números con decimales |
| Numérico | `complex` | Números complejos |
| Booleano | `bool` | `True` o `False` |
| Secuencia | `list` | Lista de elementos |
| Secuencia | `tuple` | Tupla de elementos |
| Secuencia | `range` | Secuencia de números |
| Texto | `str` | Cadenas de caracteres |
| Binario | `bytes` | Secuencia de bytes inmutable |
| Binario | `bytearray` | Secuencia de bytes modificable |
| Conjuntos | `set` | Conjunto de elementos |
| Conjuntos | `frozenset` | Conjunto inmutable |
| Iteración | `iter` | El PDF lo enumera dentro de este bloque |
| Mapas | `dict` | Datos organizados en parejas clave-valor |

En este tema basta con reconocer los nombres y comprender los tipos que se explican con más detalle.

### 6.2. Tipos numéricos

- `int`: entero, por ejemplo `7`.
- `float`: real, por ejemplo `7.5`.
- `complex`: complejo, por ejemplo `1+2j`.

Operaciones importantes:

| Operador | Operación | Ejemplo | Resultado |
|---|---|---|---|
| `/` | División normal | `7 / 2` | `3.5` |
| `//` | División entera | `7 // 2` | `3` |
| `**` | Potencia | `2 ** 3` | `8` |
| `%` | Resto | `7 % 2` | `1` |

### 6.3. Cadenas: índices

Una cadena es una secuencia de caracteres. Cada carácter tiene una posición llamada **índice**. Los índices empiezan por `0`:

```python
palabra = "Python"
print(palabra[0])  # P
print(palabra[1])  # y
```

También podemos utilizar índices negativos para contar desde el final:

```python
print(palabra[-1])  # n
print(palabra[-2])  # o
```

### 6.4. Subcadenas o slicing

Sintaxis:

```python
cadena[inicio:fin:paso]
```

- `inicio`: índice desde el que empezamos; se incluye.
- `fin`: índice donde paramos; **no se incluye**.
- `paso`: cuántas posiciones avanzamos. Si se omite, vale `1`.

Con `palabra = "Python"`:

| Expresión | Resultado | Explicación |
|---|---|---|
| `palabra[1:4]` | `"yth"` | Posiciones 1, 2 y 3 |
| `palabra[1:1]` | `""` | No recoge caracteres |
| `palabra[2:]` | `"thon"` | Desde 2 hasta el final |
| `palabra[:-2]` | `"Pyth"` | Excluye los dos últimos |
| `palabra[:]` | `"Python"` | Toda la cadena |
| `palabra[0:6:2]` | `"Pto"` | Cada dos posiciones |

### 6.5. `chr()` y `ord()`

- `chr(numero)`: devuelve el carácter correspondiente al código Unicode.
- `ord(caracter)`: devuelve el código Unicode de un carácter.

```python
print(chr(97))   # a
print(ord("a"))  # 97
```

### 6.6. Conversión de tipos

Convertir significa transformar un valor de un tipo a otro, siempre que sea posible.

| Función | Qué hace |
|---|---|
| `int(x)` | Convierte a entero |
| `float(x)` | Convierte a real |
| `complex(x)` | Crea un complejo sin parte imaginaria |
| `complex(x, y)` | Crea un complejo con parte real `x` e imaginaria `y` |

Ejemplos:

```python
print(int(7.9))        # 7
print(int("345"))      # 345
print(float(1))        # 1.0
print(float("1.234"))  # 1.234
print(complex(2, 3))   # (2+3j)
```

**Atención:** `int(7.9)` elimina la parte decimal; no redondea al entero más cercano.

Una cadena que contenga un decimal no se puede convertir directamente a entero:

```python
int("123.3")  # ValueError
```

Primero habría que convertirla a `float` si ese es el objetivo:

```python
numero = float("123.3")
```

### 6.7. `type()` e `isinstance()`

`type(objeto)` devuelve el tipo del objeto:

```python
print(type(5))       # <class 'int'>
print(type(5.5))     # <class 'float'>
print(type("Hola"))  # <class 'str'>
```

`isinstance(objeto, tipo)` comprueba si un objeto pertenece a un tipo y devuelve `True` o `False`:

```python
print(isinstance(5, int))    # True
print(isinstance(5.5, int))  # False
```

**Diferencia:** `type()` informa del tipo; `isinstance()` responde a una comprobación.

## 7. Operadores

Los operadores permiten realizar operaciones con valores y variables.

### 7.1. Operadores de asignación

El operador `=` asigna un valor a una variable:

```python
edad = 20
```

Operadores abreviados:

| Operador | Equivale a |
|---|---|
| `+=` | `x = x + valor` |
| `-=` | `x = x - valor` |
| `*=` | `x = x * valor` |
| `/=` | `x = x / valor` |
| `%=` | `x = x % valor` |
| `**=` | `x = x ** valor` |
| `//=` | `x = x // valor` |

### 7.2. Asignación múltiple

```python
a, b, c = 1, 2, "hola"
```

`a` vale `1`, `b` vale `2` y `c` vale `"hola"`.

### 7.3. Operadores aritméticos

| Operador | Significado | Ejemplo |
|---|---|---|
| `+` | Suma | `4 + 3` → `7` |
| `-` | Resta | `4 - 3` → `1` |
| `*` | Multiplicación | `4 * 3` → `12` |
| `/` | División normal | `7 / 2` → `3.5` |
| `//` | División entera | `7 // 2` → `3` |
| `%` | Resto | `7 % 2` → `1` |
| `**` | Potencia | `2 ** 3` → `8` |

Los signos `+` y `-` también pueden utilizarse como operadores unarios: `-5`, `+5`.

### 7.4. Operadores de comparación

Comparan dos valores y devuelven `True` o `False`.

| Operador | Significado |
|---|---|
| `==` | Igual |
| `!=` | Distinto |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

```python
edad = 20
print(edad >= 18)  # True
print(edad == 15)  # False
```

### 7.5. Operadores lógicos

| Operador | Significado |
|---|---|
| `and` | Verdadero si las dos condiciones son verdaderas |
| `or` | Verdadero si al menos una condición es verdadera |
| `not` | Invierte el valor lógico |

```python
edad = 20
tiene_entrada = True

print(edad >= 18 and tiene_entrada)  # True
print(edad < 18 or tiene_entrada)    # True
print(not tiene_entrada)             # False
```

Python utiliza evaluación de cortocircuito: con `and`, si lo primero es falso ya no necesita evaluar lo segundo; con `or`, si lo primero es verdadero tampoco necesita evaluar lo segundo.

### 7.6. `all()` y `any()`

- `all(iterable)`: devuelve `True` si todos los elementos son verdaderos. También devuelve `True` si está vacío.
- `any(iterable)`: devuelve `True` si al menos uno es verdadero. Devuelve `False` si está vacío.

```python
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(any([False, False, True])) # True
print(any([False, False]))       # False
```

### 7.7. Operadores de cadenas

- `+`: concatena, es decir, une cadenas.
- `*`: repite una cadena un número de veces.

```python
print("Hola " + "DAW")  # Hola DAW
print("Ja" * 3)         # JaJaJa
```

Dos literales de cadena escritos uno al lado del otro se unen automáticamente:

```python
texto = ("Hola, "
         "estudiante")
print(texto)  # Hola, estudiante
```

Esto funciona con literales, no con variables colocadas una al lado de otra sin operador.

### 7.8. Operadores de pertenencia

- `in`: devuelve `True` si el valor está dentro de la secuencia.
- `not in`: devuelve `True` si no está.

```python
palabra = "Python"
print("P" in palabra)      # True
print("z" not in palabra)  # True
```

### 7.9. Operadores de identidad

- `is`: comprueba si dos referencias apuntan al mismo objeto.
- `is not`: comprueba si apuntan a objetos distintos.

No debe confundirse identidad (`is`) con igualdad (`==`):

- `==` compara si los valores son iguales.
- `is` comprueba si es exactamente el mismo objeto.

Para comparar valores normalmente debemos utilizar `==`. Para comprobar si una variable contiene `None`, es habitual utilizar `is None`.

### 7.10. Operadores a nivel de bit

Trabajan sobre la representación binaria de números enteros:

| Operador | Operación |
|---|---|
| `&` | AND bit a bit |
| `\|` | OR bit a bit |
| `^` | XOR bit a bit |
| `<<` | Desplazamiento a la izquierda |
| `>>` | Desplazamiento a la derecha |
| `~` | Inversión de bits |

Ejemplo:

```python
a = 5  # 0101 en binario
b = 3  # 0011 en binario

print(a & b)  # 1
print(a | b)  # 7
print(a ^ b)  # 6
```

Este apartado aparece en el PDF; si todavía no lo habéis trabajado, basta inicialmente con reconocer los operadores y su finalidad.

## 8. Objetos mutables e inmutables

En Python, las variables hacen referencia a objetos. Algunos objetos se pueden modificar y otros no.

### 8.1. Objetos inmutables

Un objeto **inmutable** no permite cambiar su contenido una vez creado.

Ejemplos principales del material:
- Números (`int`, `float`, etc.).
- Cadenas (`str`).
- Tuplas (`tuple`).

Ejemplo con una cadena:

```python
texto = "Hola"
texto[0] = "h"  # Error: no se puede cambiar un carácter
```

Para obtener otro texto debemos crear una nueva cadena:

```python
texto = "hola"
```

### 8.2. Objetos mutables

Un objeto **mutable** permite modificar su contenido después de crearlo.

Ejemplos principales indicados en el PDF:
- Listas (`list`).
- Diccionarios (`dict`).

```python
numeros = [1, 2]
numeros[0] = 5
print(numeros)  # [5, 2]
```

### 8.3. Dos variables que apuntan al mismo objeto

```python
a = [1, 2]
b = a

a[0] = 5

print(a)  # [5, 2]
print(b)  # [5, 2]
```

`b = a` no crea una lista nueva: ambas variables hacen referencia a la misma lista. Por eso el cambio se observa desde los dos nombres.

### 8.4. Función `id()`

`id(objeto)` devuelve un identificador del objeto durante su vida. Sirve para observar si dos variables se refieren al mismo objeto:

```python
a = [1, 2]
b = a

print(id(a))
print(id(b))
```

Los dos identificadores serán iguales porque `a` y `b` apuntan a la misma lista. El número concreto puede cambiar entre ejecuciones.

## 9. Entrada y salida estándar

### 9.1. Entrada: `input()`

`input()` permite leer información que escribe el usuario por teclado.

Sintaxis:

```python
variable = input("Mensaje que aparece: ")
```

**Importante:** `input()` devuelve siempre una cadena (`str`), aunque el usuario escriba números.

Ejemplo:

```python
nombre = input("Nombre: ")
print("Hola", nombre)
```

Para trabajar con un número debemos convertir el texto:

```python
edad = int(input("Edad: "))
precio = float(input("Precio: "))
```

Si el usuario escribe un texto que no se puede convertir, se producirá un `ValueError`.

### 9.2. Salida: `print()`

`print()` muestra información en la salida estándar, normalmente la consola.

```python
print(valor1, valor2, valor3)
```

Por defecto:
- Separa los valores con un espacio.
- Termina con un salto de línea (`\n`).

**Parámetro `sep`:** indica el separador entre los valores.

```python
print(1, 2, 3, sep="-")
```

Resultado: `1-2-3`.

**Parámetro `end`:** indica qué se escribe al final. Por defecto es `\n`.

```python
print(1, 2, 3, sep="-", end=".")
print("Fin")
```

Resultado:
```text
1-2-3.Fin
```

### 9.3. Concatenar texto y números

No podemos unir directamente una cadena y un entero con `+`:

```python
edad = 20
# print("Edad: " + edad)  # TypeError
```

Podemos convertir el número a cadena con `str()`:

```python
print("Edad: " + str(edad))
```

También podemos pasar varios valores a `print()` separados por comas:

```python
print("Edad:", edad)
```

### 9.4. Formatear cadenas

El PDF presenta el estilo antiguo con `%` y el método `format()`.

**Estilo antiguo:**

```python
print("%d %f %s" % (2.5, 2.5, 2.5))
print("Producto %s, cantidad=%d, precio=%.2f" % ("cesta", 23, 13.456))
```

Marcadores que aparecen en los ejemplos:
- `%d`: entero.
- `%f`: número real.
- `%s`: cadena.
- `%.2f`: número real con dos decimales.

**Método `format()`:**

Los marcadores `{}` indican dónde se colocarán los valores:

```python
print("Un {} vale {} {}".format("€", 1.12, "$"))
```

Se puede indicar la posición:

```python
print("Un {2} vale {1} {0}".format("€", 1.12, "$"))
```

O utilizar nombres:

```python
print("Un {moneda1} vale {cambio} {moneda2}".format(
    moneda1="€", cambio=1.12, moneda2="$"
))
```

También podemos indicar anchura y alineación:

| Formato | Significado |
|---|---|
| `{:n}` | Alineación izquierda en una anchura de `n` |
| `{:>n}` | Alineación derecha |
| `{:^n}` | Alineación centrada |
| `{:nd}` | Entero con anchura `n` |
| `{:n.mf}` | Real con anchura `n` y `m` decimales |

Ejemplos:

```python
print("|{:<10}|".format("lunes"))
print("|{:>10}|".format("lunes"))
print("|{:^10}|".format("lunes"))
print("Cantidad {:5d}".format(12))
print("Pi vale {:8.4f}".format(3.141592))
```

## 10. Funciones predefinidas

Son funciones que Python ya incluye y que podemos utilizar sin programarlas nosotros.

### 10.1. Funciones numéricas

| Función | Para qué sirve | Ejemplo |
|---|---|---|
| `abs(x)` | Valor absoluto | `abs(-5)` → `5` |
| `divmod(x, y)` | Devuelve división entera y resto en una tupla | `divmod(7, 2)` → `(3, 1)` |
| `hex(x)` | Representación hexadecimal | `hex(15)` → `'0xf'` |
| `oct(x)` | Representación octal | `oct(8)` → `'0o10'` |
| `bin(x)` | Representación binaria | `bin(5)` → `'0b101'` |
| `pow(x, y)` | Potencia | `pow(2, 3)` → `8` |
| `round(x, y)` | Redondeo, opcionalmente con `y` decimales | `round(7.567, 1)` → `7.6` |

### 10.2. Funciones y métodos de cadenas

| Elemento | Para qué sirve | Ejemplo |
|---|---|---|
| `len(c)` | Cuenta caracteres | `len("Hola")` → `4` |
| `min(c)` | Devuelve el carácter menor según su orden Unicode | `min("casa")` → `'a'` |
| `max(c)` | Devuelve el carácter mayor según su orden Unicode | `max("casa")` → `'s'` |
| `c.upper()` | Convierte a mayúsculas | `"hola".upper()` → `'HOLA'` |
| `c.lower()` | Convierte a minúsculas | `"HOLA".lower()` → `'hola'` |
| `c.title()` | Pone en mayúscula inicial las palabras | `"hola mundo".title()` → `'Hola Mundo'` |
| `c.split(delimitador)` | Divide una cadena y devuelve una lista | `"A,B".split(",")` → `['A', 'B']` |

`upper()`, `lower()`, `title()` y `split()` son métodos de las cadenas: se escriben después de la cadena y un punto.

Ejemplo:

```python
datos = "Ana,20,Madrid"
partes = datos.split(",")
print(partes)
```

Resultado:
```text
['Ana', '20', 'Madrid']
```

Si no indicamos delimitador, `split()` separa utilizando espacios en blanco.

## 11. Chuleta final

```python
# Variables y tipos
nombre = "Ana"
edad = 20
type(edad)
isinstance(edad, int)

# Entrada y conversion
nombre = input("Nombre: ")
edad = int(input("Edad: "))
precio = float(input("Precio: "))

# Salida
print(nombre, edad)
print(1, 2, 3, sep="-", end=".")

# Cadenas
texto = "Python"
texto[0]       # Primer caracter
texto[-1]      # Ultimo caracter
texto[1:4]     # Desde 1 hasta antes de 4
len(texto)
texto.upper()
texto.lower()
texto.split(",")

# Operadores
+  -  *  /  //  %  **
== != > < >= <=
and or not
in not in
is is not

# Mutabilidad
lista = [1, 2]
lista[0] = 9

# Funciones numericas
abs(-5)
divmod(7, 2)
bin(5)
oct(8)
hex(15)
pow(2, 3)
round(7.567, 1)
```

### Diferencias que suelen preguntar

| No confundir | Diferencia |
|---|---|
| `=` y `==` | Asignar un valor frente a comparar igualdad |
| `/` y `//` | División normal frente a división entera |
| `==` y `is` | Igualdad de valor frente a identidad del objeto |
| `input()` y `int(input())` | Texto leído frente a conversión a entero |
| `type()` y `isinstance()` | Consultar tipo frente a comprobar pertenencia a un tipo |
| Mutable e inmutable | Se puede modificar el objeto frente a no poder modificarlo |
| `sep` y `end` | Separador entre valores frente a final de `print()` |
| `upper()` y `lower()` | Mayúsculas frente a minúsculas |
| `in` y `not in` | Está contenido frente a no está contenido |

### Errores habituales

1. Olvidar que `input()` devuelve `str`.
2. Intentar sumar directamente texto y números con `+`.
3. Utilizar coma decimal en un literal `float`: en Python se utiliza punto.
4. Pensar que `int(7.9)` redondea: devuelve `7`.
5. Pensar que el índice de una cadena empieza en `1`: empieza en `0`.
6. Pensar que el límite final de un slicing se incluye: no se incluye.
7. Confundir `is` con `==`.
8. Intentar cambiar un carácter de una cadena.
9. Olvidar la indentación de un bloque.
10. Mezclar tabulaciones y espacios.
11. Pensar que `b = a` crea una copia de una lista: ambas variables apuntan a la misma lista.
12. Olvidar que `print()` separa por espacios y termina con salto de línea por defecto.

## 12. Aclaraciones sobre el PDF

Se conserva la organización y los contenidos del documento del profesor. Estas notas aclaran algunos puntos:

1. **Triple comilla y comentarios:** las cadenas multilínea no son comentarios ignorados como `#`. Se utilizan, entre otros usos, para documentar módulos, clases y funciones.
2. **Constantes:** escribir el nombre en mayúsculas es una convención, no una protección del lenguaje que impida cambiar el valor.
3. **Operador `is`:** el ejemplo del PDF `b is 6` no es una forma correcta de comprobar si `b` vale 6. Para comparar valores se debe escribir `b == 6`. La identidad comprueba si dos referencias apuntan al mismo objeto.
4. **Operador `/`:** el resultado es de tipo `float` en Python 3, incluso cuando la división es exacta; por ejemplo, `6 / 2` da `3.0`.
5. **`round()`:** en los casos de empate Python aplica reglas de redondeo específicas; para los ejemplos básicos del tema, se puede entender como redondeo al número de decimales indicado.
6. **`min()` y `max()` sobre cadenas:** comparan caracteres según su orden Unicode, no según el significado lingüístico de las palabras.
7. **Tipos enumerados:** `iter` se entiende mejor como una función incorporada que obtiene un iterador, no como una clase de conjunto equivalente a `set` o `frozenset`.

Estas aclaraciones son complementarias: no sustituyen el temario del profesor ni amplían el tema con contenidos avanzados.

---

**Archivos de práctica:** consulta los `.py` que acompañan a este documento. Cada archivo trabaja un bloque concreto y puede ejecutarse de forma independiente, salvo el ejemplo de módulos de constantes, que utiliza dos archivos.
