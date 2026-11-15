# TEMA 3. CONTROL DE FLUJO — PYTHON

**Asignatura:** Desarrollo de Aplicaciones Web  
**Módulo:** Programación en Python  
**Material de referencia:** Rosa Rodríguez García

---

# 1. ¿Qué es el control de flujo?

El **control de flujo** permite decidir qué instrucciones ejecuta un programa y cuántas veces las ejecuta.

Por ejemplo:
- Ejecutar unas instrucciones solamente si se cumple una condición.
- Elegir entre varias alternativas.
- Repetir instrucciones mientras se cumpla una condición.
- Recorrer los elementos de una secuencia.
- Agrupar instrucciones en funciones para reutilizarlas.

En este tema estudiaremos:
1. Condicionales (`if`, `elif`, `else`).
2. Expresión reducida del `if`.
3. Selección con `match-case`.
4. Bucles `while` y `for`.
5. `break` y `continue`.
6. Recorrido de varias secuencias con `zip()`.
7. Funciones (`def` y `return`).
8. Variables locales y globales.
9. Parámetros posicionales, valores por defecto y argumentos con nombre.
10. Argumentos arbitrarios (`*args` y `**kwargs`).
11. Devolver varios resultados.

---

# 2. Condicionales

Los **condicionales** permiten ejecutar un bloque de instrucciones dependiendo de si una condición se cumple o no.

En Python, los bloques se identifican mediante la **indentación**: las instrucciones que pertenecen al `if`, `elif` o `else` deben llevar sangría.

## 2.1. Alternativa simple: `if`

Se utiliza cuando queremos ejecutar unas instrucciones únicamente si una condición es verdadera.

**Sintaxis:**

```python
if condicion:
    instrucciones
```

- `if`: inicia la condición.
- `condicion`: expresión que devuelve `True` o `False`.
- `:`: indica el comienzo del bloque.
- `instrucciones`: código que se ejecuta si la condición es verdadera.

**Ejemplo:**

```python
numero = -5

if numero < 0:
    print("El número es negativo")
```

**Resultado:**
```text
El número es negativo
```

Si `numero` fuese 5, no aparecería ningún mensaje porque la condición sería falsa.

## 2.2. Alternativa doble: `if-else`

Se utiliza cuando tenemos dos posibilidades:
- Si la condición es verdadera, ejecutamos el bloque del `if`.
- Si es falsa, ejecutamos el bloque del `else`.

**Sintaxis:**

```python
if condicion:
    instrucciones_si_verdadero
else:
    instrucciones_si_falso
```

**Ejemplo:**

```python
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

**Resultado:**
```text
Eres menor de edad
```

## 2.3. Alternativa múltiple: `if-elif-else`

Se utiliza cuando necesitamos comprobar varias condiciones.

- `if`: comprueba la primera condición.
- `elif`: comprueba otra condición si las anteriores no se han cumplido.
- `else`: se ejecuta si ninguna condición anterior se cumple.

**Sintaxis:**

```python
if condicion1:
    instrucciones
elif condicion2:
    instrucciones
elif condicion3:
    instrucciones
else:
    instrucciones_por_defecto
```

**Ejemplo:**

```python
numero = 0

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
```

**Resultado:**
```text
El número es cero
```

**Importante:** Python comprueba las condiciones en orden. Cuando encuentra una verdadera, ejecuta su bloque y no sigue comprobando las siguientes.

## 2.4. Expresión reducida del `if`

Permite escribir una alternativa sencilla en una sola línea y guardar directamente el resultado en una variable.

**Sintaxis:**

```python
variable = valor_si_verdadero if condicion else valor_si_falso
```

**Ejemplo:**

```python
idioma = "es"

saludo = "HOLA" if idioma == "es" else "HI"

print(saludo)
```

**Resultado:**
```text
HOLA
```

La expresión significa:
- Si `idioma == "es"` es verdadero, `saludo` recibe `"HOLA"`.
- En caso contrario, recibe `"HI"`.

No conviene utilizar esta forma cuando hay muchas condiciones o instrucciones.

---

# 3. Selección con `match-case`

`match-case` permite comparar una variable con distintos patrones y ejecutar el bloque correspondiente.

Es una alternativa útil cuando queremos comprobar distintos valores posibles.

**Sintaxis general:**

```python
match variable:
    case patron1:
        instrucciones
    case patron2:
        instrucciones
    case _:
        instrucciones_por_defecto
```

- `match`: indica qué variable vamos a comparar.
- `case`: define un patrón que queremos comprobar.
- `_`: es el patrón comodín; se utiliza como caso predeterminado.

**Ejemplo:**

```python
opcion = 2

match opcion:
    case 1:
        print("Has elegido el menú de inicio")
    case 2:
        print("Has elegido la configuración")
    case 3:
        print("Has elegido salir")
    case _:
        print("Opción no válida")
```

**Resultado:**
```text
Has elegido la configuración
```

## 3.1. Varios valores en un mismo `case`

El operador `|` permite indicar varios patrones para un mismo bloque.

```python
numero = 20

match numero:
    case 10 | 20 | 30:
        print("El número es 10, 20 o 30")
    case _:
        print("Otro número")
```

**Resultado:**
```text
El número es 10, 20 o 30
```

## 3.2. Patrones de listas

También se pueden comprobar estructuras como listas y recoger sus elementos en variables.

```python
datos = [10, 20]

match datos:
    case [x, y]:
        print("Lista de dos elementos:", x, y)
    case [x, y, z]:
        print("Lista de tres elementos:", x, y, z)
    case _:
        print("Formato desconocido")
```

**Resultado:**
```text
Lista de dos elementos: 10 20
```

## 3.3. Condiciones adicionales con `if`

Un patrón puede incluir una condición adicional mediante `if`. Se conoce como guarda.

```python
numero = 10

match numero:
    case 10 if numero % 2 == 0:
        print("Es 10 y además es par")
    case 10:
        print("Es 10, pero no es par")
    case _:
        print("No es 10")
```

**Resultado:**
```text
Es 10 y además es par
```

**Nota:** `match-case` está disponible desde Python 3.10.

---

# 4. Bucles

Los **bucles** permiten repetir un bloque de instrucciones varias veces.

En este tema aparecen:
- `while`: repite mientras una condición sea verdadera.
- `for`: recorre los elementos de un elemento iterable, como una cadena, lista, tupla, diccionario o rango.

## 4.1. Bucle `while`

El bucle `while` repite las instrucciones mientras la condición sea verdadera.

**Sintaxis:**

```python
while condicion:
    instrucciones
```

**Ejemplo:**

```python
año = 2001

while año <= 2005:
    print("Informes del año", año)
    año += 1
```

**Resultado:**
```text
Informes del año 2001
Informes del año 2002
Informes del año 2003
Informes del año 2004
Informes del año 2005
```

`año += 1` aumenta el valor de `año` en una unidad. Es equivalente a `año = año + 1`.

**Cuidado:** si la condición nunca llega a ser falsa y no existe una salida del bucle, tendremos un bucle infinito.

## 4.2. `while-else`

Python permite añadir un bloque `else` a un bucle `while`.

El `else` se ejecuta cuando el bucle termina porque su condición se vuelve falsa.

```python
numero = 1

while numero <= 3:
    print(numero)
    numero += 1
else:
    print("Hemos terminado")
```

**Resultado:**
```text
1
2
3
Hemos terminado
```

Si el bucle termina mediante `break`, el bloque `else` no se ejecuta.

## 4.3. Bucle `for`

El bucle `for` recorre los elementos de un iterable, como una cadena, lista, tupla, diccionario o rango.

**Sintaxis:**

```python
for variable in elemento_a_recorrer:
    instrucciones
```

En cada vuelta, la variable recibe el siguiente elemento.

**Ejemplo con `range()`:**

```python
for i in range(1, 5):
    print(i)
```

**Resultado:**
```text
1
2
3
4
```

`range(1, 5)` empieza en 1 y llega hasta 4. El valor final (5) no se incluye.

Otro ejemplo:

```python
for i in range(5):
    print(i)
```

**Resultado:**
```text
0
1
2
3
4
```

Cuando se indica un único número, `range(5)` comienza en 0 y termina en 4.

## 4.4. `for-else`

También podemos añadir `else` a un bucle `for`.

El bloque `else` se ejecuta cuando el recorrido termina normalmente. Si se utiliza `break`, no se ejecuta.

```python
for numero in range(1, 4):
    print(numero)
else:
    print("Hemos terminado")
```

**Resultado:**
```text
1
2
3
Hemos terminado
```

---

# 5. `break` y `continue`

Son instrucciones que modifican el comportamiento de un bucle.

## 5.1. `break`

Termina inmediatamente el bucle en el que se encuentra.

**Ejemplo:**

```python
for numero in range(1, 6):
    if numero == 3:
        break
    print(numero)
```

**Resultado:**
```text
1
2
```

Cuando `numero` vale 3, se ejecuta `break` y el bucle termina.

**Importante:** si el bucle tiene un `else`, `break` impide que se ejecute ese `else`.

## 5.2. `continue`

Finaliza la vuelta actual y pasa directamente a la siguiente iteración del bucle.

**Ejemplo:**

```python
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)
```

**Resultado:**
```text
1
2
4
5
```

Cuando `numero` vale 3, `continue` evita que se ejecute el `print()` de esa vuelta. El bucle continúa con el siguiente número.

**Diferencia fundamental:**

| Instrucción | Qué hace |
|---|---|
| `break` | Termina todo el bucle. |
| `continue` | Salta la vuelta actual y continúa el bucle. |

---

# 6. Recorrer varias secuencias: `zip()`

La función `zip()` permite recorrer varias secuencias al mismo tiempo.

En cada iteración agrupa los elementos que ocupan la misma posición y los entrega juntos en una tupla.

**Sintaxis:**

```python
for variable1, variable2 in zip(secuencia1, secuencia2):
    instrucciones
```

**Ejemplo:**

```python
numeros = range(1, 5)
nombres = ["Ana", "Juan", "Pepe"]

for numero, nombre in zip(numeros, nombres):
    print(numero, nombre)
```

**Resultado:**
```text
1 Ana
2 Juan
3 Pepe
```

**Importante:** el recorrido termina cuando se acaba la secuencia más corta. En este ejemplo, `nombres` tiene tres elementos, por eso solo se realizan tres iteraciones.

---

# 7. Funciones

Una **función** es un bloque de código que realiza una tarea concreta y que podemos reutilizar llamándolo por su nombre.

Las funciones ayudan a organizar el programa y evitar repetir código.

## 7.1. Definir una función: `def`

Para crear una función utilizamos la palabra reservada `def`.

**Sintaxis:**

```python
def nombre_funcion(parametros):
    instrucciones
```

- `def`: indica que vamos a definir una función.
- `nombre_funcion`: nombre que tendrá la función.
- `parametros`: datos que puede recibir.
- `:`: comienza el bloque de la función.

**Ejemplo:**

```python
def saludar():
    print("Hola, bienvenido")

saludar()
```

**Resultado:**
```text
Hola, bienvenido
```

Definir una función no significa que se ejecute automáticamente. Para ejecutarla hay que llamarla escribiendo su nombre y los paréntesis.

## 7.2. Funciones con parámetros

Los parámetros permiten que una función reciba datos para trabajar con ellos.

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Ana")
saludar("Juan")
```

**Resultado:**
```text
Hola Ana
Hola Juan
```

`nombre` es el parámetro de la función. `"Ana"` y `"Juan"` son argumentos que proporcionamos al llamarla.

## 7.3. Devolver un resultado con `return`

`return` permite devolver un resultado al lugar desde el que se llamó a la función.

```python
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(4, 5)
print(total)
```

**Resultado:**
```text
9
```

La función calcula la suma y devuelve el resultado. Después, ese resultado se guarda en `total`.

**Diferencia entre `print()` y `return`:**
- `print()` muestra información por pantalla.
- `return` devuelve un valor para que el programa pueda utilizarlo.

## 7.4. Ejemplo: factorial

El factorial de un número positivo se calcula multiplicando todos los enteros desde 1 hasta ese número. Por convenio, el factorial de 0 es 1.

```python
def factorial(n):
    """Calcula el factorial de un número."""
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

print(factorial(5))
```

**Resultado:**
```text
120
```

Cálculo: `1 * 2 * 3 * 4 * 5 = 120`.

---

# 8. Variables locales y globales

El ámbito de una variable indica desde dónde se puede utilizar.

## 8.1. Variables locales

Una variable creada dentro de una función es local a esa función. Normalmente solo puede utilizarse dentro de ella.

```python
def operar(a, b):
    suma = a + b
    resta = a - b
    print(suma, resta)

operar(4, 5)
```

**Resultado:**
```text
9 -1
```

La variable `resta` se creó dentro de `operar()`. Si intentamos utilizarla fuera, Python dará un error `NameError`.

## 8.2. Variables globales

Una variable global se define fuera de las funciones y puede consultarse desde ellas.

```python
PI = 3.1415

def area(radio):
    return PI * radio ** 2

print(area(2))
```

**Resultado:**
```text
12.566
```

En los apuntes se recomienda escribir las constantes globales en mayúsculas, como `PI`.

## 8.3. La palabra `global`

Si queremos modificar desde una función una variable global, podemos utilizar `global`.

```python
suma = 0

def operar(a, b):
    global suma
    suma = a + b

operar(4, 5)
print(suma)
```

**Resultado:**
```text
9
```

`global suma` indica que dentro de la función vamos a utilizar la variable global `suma`, no crear una variable local nueva.

**Consejo:** utiliza variables locales siempre que sea posible. Las variables globales pueden hacer que un programa sea más difícil de entender y mantener.

---

# 9. Paso de parámetros

Los parámetros son los datos que recibe una función. Al llamar a una función, proporcionamos argumentos.

En el material de clase se explica que Python trabaja con objetos y referencias: una variable referencia a un objeto, en lugar de ser simplemente una caja que contiene un valor.

**Ejemplo sencillo:**

```python
def mostrar(numero):
    print(numero)

valor = 10
mostrar(valor)
```

**Resultado:**
```text
10
```

**Aclaración importante sobre el material:** decir que Python pasa siempre los parámetros «por referencia» puede llevar a confusión. Una descripción más precisa es que Python pasa referencias a objetos (también llamado *call by sharing*). Esto no funciona exactamente igual que el paso por referencia de algunos otros lenguajes.

---

# 10. Parámetros con valores por defecto y argumentos con nombre

Son dos conceptos relacionados, pero no son exactamente lo mismo.

## 10.1. Parámetros con valor por defecto

Al definir una función podemos asignar un valor inicial a un parámetro. Si al llamar a la función no indicamos ese argumento, se utiliza el valor por defecto.

**Sintaxis:**

```python
def nombre_funcion(parametro, otro_parametro=valor):
    instrucciones
```

**Ejemplo:**

```python
def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Ana")
saludar("Juan", "Buenos días")
```

**Resultado:**
```text
Hola Ana
Buenos días Juan
```

En la primera llamada se utiliza el valor por defecto `"Hola"`. En la segunda se proporciona otro valor.

## 10.2. Argumentos con nombre (*keyword arguments*)

Podemos indicar el nombre del parámetro al llamar a una función. Así no dependemos del orden de esos argumentos con nombre.

```python
def presentar(nombre, edad):
    print(nombre, edad)

presentar(edad=20, nombre="Ana")
```

**Resultado:**
```text
Ana 20
```

## 10.3. Ejemplo de la profesora: función `operar`

```python
def operar(n1, n2, operador="+", respuesta="El resultado es "):
    if operador == "+":
        return respuesta + str(n1 + n2)
    elif operador == "-":
        return respuesta + str(n1 - n2)
    else:
        return "Error"

print(operar(5, 7))
print(operar(4, 6, respuesta="La suma es "))
print(operar(4, 6, respuesta="La resta es ", operador="-"))
```

**Resultado:**
```text
El resultado es 12
La suma es 10
La resta es -2
```

En este ejemplo:
- `n1` y `n2` son parámetros obligatorios.
- `operador` y `respuesta` tienen valores por defecto.
- En las llamadas podemos cambiar los valores por defecto indicando el nombre del argumento.

**Regla de orden:** al definir una función, los parámetros obligatorios deben ir antes que los parámetros con valor por defecto. Al llamar a una función, los argumentos posicionales deben ir antes que los argumentos con nombre.

---

# 11. Argumentos arbitrarios: `*args` y `**kwargs`

Permiten definir funciones que reciben un número variable de argumentos.

## 11.1. `*args`

Se utiliza cuando queremos recibir un número indefinido de argumentos posicionales.

Los argumentos se agrupan dentro de una tupla llamada `args` (el nombre `args` es una convención; lo importante es el `*`).

**Sintaxis:**

```python
def nombre_funcion(*args):
    instrucciones
```

**Ejemplo:**

```python
def sumar(*args):
    resultado = 0

    for numero in args:
        resultado += numero

    return resultado

print(sumar(2))
print(sumar(2, 3, 4))
print(sumar(1, 2, 3, 4, 5))
```

**Resultado:**
```text
2
9
15
```

La función puede recibir uno, varios o muchos números.

## 11.2. `**kwargs`

Se utiliza para recibir un número indefinido de argumentos con nombre.

Estos argumentos se agrupan en un diccionario.

**Sintaxis:**

```python
def nombre_funcion(**kwargs):
    instrucciones
```

**Ejemplo:**

```python
def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)

mostrar_datos(nombre="Ana", edad=20, ciudad="Madrid")
```

**Resultado:**
```text
nombre Ana
edad 20
ciudad Madrid
```

- `clave` contiene el nombre del argumento.
- `valor` contiene el valor que hemos indicado.
- `.items()` permite recorrer las parejas clave-valor del diccionario.

**Diferencia:**

| Forma | Qué recoge | Tipo de agrupación |
|---|---|---|
| `*args` | Argumentos posicionales variables | Tupla |
| `**kwargs` | Argumentos con nombre variables | Diccionario |

---

# 12. Devolver múltiples resultados

Una función puede devolver más de un dato. En Python podemos separarlos mediante comas; Python los agrupa en una tupla.

**Ejemplo:**

```python
def operar(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2

resultados = operar(5, 2)

print(resultados)
```

**Resultado:**
```text
(7, 3, 10)
```

También podemos guardar cada resultado en una variable mediante el desempaquetado:

```python
def operar(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2

suma, resta, producto = operar(5, 2)

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
```

**Resultado:**
```text
Suma: 7
Resta: 3
Producto: 10
```

El orden importa:
- Primer resultado → `suma`.
- Segundo resultado → `resta`.
- Tercer resultado → `producto`.

El número de variables debe coincidir con el número de valores devueltos.

---

# 13. Errores habituales y trampas de examen

1. **Olvidar los dos puntos (`:`):** después de `if`, `elif`, `else`, `while`, `for`, `def`, `match` y `case` se necesitan dos puntos.
2. **Olvidar la indentación:** el bloque debe estar correctamente sangrado.
3. **Confundir `=` y `==`:** `=` asigna un valor; `==` compara dos valores.
4. **Confundir el final de `range()`:** el límite final no se incluye.
5. **Crear un `while` infinito:** comprueba que la condición pueda llegar a ser falsa.
6. **Confundir `break` y `continue`:** `break` termina el bucle; `continue` solo salta la iteración actual.
7. **Pensar que el `else` de un bucle funciona como el de un `if`:** en un bucle se ejecuta al terminar normalmente, pero no cuando se sale con `break`.
8. **Intentar utilizar una variable local fuera de su función:** puede producir `NameError`.
9. **Olvidar `return`:** si necesitamos que una función entregue un resultado, debemos devolverlo.
10. **Confundir `print()` con `return`:** mostrar un valor no es lo mismo que devolverlo.
11. **Colocar un parámetro obligatorio después de uno con valor por defecto:** el orden de los parámetros en la definición importa.
12. **Confundir `*args` con `**kwargs`:** el primero agrupa argumentos posicionales en una tupla; el segundo agrupa argumentos con nombre en un diccionario.
13. **Olvidar que `zip()` termina con la secuencia más corta.**
14. **Usar `match-case` en una versión anterior a Python 3.10:** esa sintaxis requiere Python 3.10 o posterior.

---

# 14. Chuleta rápida

| Elemento | Para qué sirve |
|---|---|
| `if` | Ejecutar código si se cumple una condición. |
| `elif` | Comprobar otra condición. |
| `else` | Ejecutar el caso alternativo. |
| `valor_a if condicion else valor_b` | Escribir un `if` sencillo en una expresión. |
| `match-case` | Comparar una variable con distintos patrones. |
| `case _` | Caso predeterminado. |
| `while` | Repetir mientras una condición sea verdadera. |
| `for` | Recorrer elementos. |
| `range()` | Generar una secuencia de números. |
| `break` | Terminar el bucle. |
| `continue` | Saltar a la siguiente iteración. |
| `zip()` | Recorrer varias secuencias a la vez. |
| `def` | Definir una función. |
| `return` | Devolver un resultado. |
| `global` | Indicar que se utiliza una variable global. |
| `*args` | Recibir argumentos posicionales variables. |
| `**kwargs` | Recibir argumentos con nombre variables. |

## Sintaxis para memorizar

```python
# Condicional
if condicion:
    instrucciones
elif otra_condicion:
    instrucciones
else:
    instrucciones

# Match-case
match variable:
    case valor:
        instrucciones
    case _:
        instrucciones

# While
while condicion:
    instrucciones

# For
for elemento in iterable:
    instrucciones

# Función
def nombre(parametros):
    instrucciones
    return resultado

# Parámetro con valor por defecto
def nombre(parametro=valor):
    instrucciones

# Argumentos variables
def nombre(*args):
    instrucciones

def nombre(**kwargs):
    instrucciones
```

---

# 15. Observaciones sobre el material original

Estas aclaraciones no sustituyen los apuntes de clase; sirven para evitar aprender una errata o una explicación confusa.

- **Alternativas múltiples:** en el ejemplo original aparecen intercambiados los mensajes de positivo y negativo. La condición `numero > 0` corresponde a positivo y `numero < 0` a negativo.
- **Sintaxis de los ejemplos:** algunos fragmentos del documento omiten los dos puntos o la indentación al copiar el código. En Python son obligatorios.
- **`for i in range(5)`:** en el documento falta el carácter `:` al final de la línea.
- **`match-case`:** el último ejemplo de la profesora queda incompleto en el documento después de `case _:`. Se ha completado con un mensaje de salida para que el ejemplo sea ejecutable.
- **Parámetros keyword:** el documento mezcla parámetros con valor por defecto y argumentos keyword. Son conceptos relacionados, pero distintos; se han explicado por separado.
- **Paso de parámetros:** la expresión «siempre por referencia» es una simplificación. Es más preciso decir que Python pasa referencias a objetos.
- **`**kwargs`:** el documento menciona su uso, pero no incluye un ejemplo completo. Se añade uno sencillo para poder practicarlo.

**Fin del tema 3. Control de flujo.**
