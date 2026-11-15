# Módulo `random` de Python — Chuleta y apuntes

## 1. ¿Para qué sirve `random`?

El módulo `random` permite trabajar con valores aleatorios o pseudoaleatorios. Se utiliza, por ejemplo, para:

- Generar números aleatorios.
- Elegir un elemento al azar de una lista o tupla.
- Elegir varios elementos al azar.
- Mezclar los elementos de una lista.
- Obtener números decimales aleatorios.

**Importante:** los resultados de `random` son pseudoaleatorios. Para los ejercicios habituales de clase y juegos sencillos, normalmente se utiliza este módulo.

## 2. Importar el módulo

Hay dos formas habituales:

```python
import random

numero = random.randint(1, 10)
print(numero)
```

Con `import random`, se escribe `random.` delante de cada función.

También se puede importar una función concreta:

```python
from random import randint

numero = randint(1, 10)
print(numero)
```

Con `from random import randint`, se puede escribir directamente `randint()`.

---

# 3. Funciones principales de `random`

## 3.1 `randint(a, b)` — Entero aleatorio

Genera un número entero aleatorio entre `a` y `b`, **incluyendo los dos límites**.

**Sintaxis:**

```python
random.randint(inicio, final)
```

**Ejemplo:**

```python
import random

numero = random.randint(1, 10)
print(numero)
```

El resultado puede ser cualquier entero desde 1 hasta 10, ambos incluidos.

Por ejemplo, podría salir `1`, `5` o `10`.

**Recuerda:** `randint(1, 10)` puede devolver 10.

## 3.2 `randrange(inicio, final, paso)` — Entero dentro de un rango

Devuelve un entero elegido entre los valores de una secuencia. El límite final **no se incluye**.

**Sintaxis:**

```python
random.randrange(inicio, final, paso)
```

- `inicio`: primer valor posible.
- `final`: límite que no se incluye.
- `paso`: separación entre los valores posibles; es opcional y por defecto vale 1.

**Ejemplo:**

```python
import random

numero = random.randrange(1, 10)
print(numero)
```

Puede devolver del 1 al 9, pero nunca el 10.

**Ejemplo con paso:**

```python
numero = random.randrange(2, 12, 2)
print(numero)
```

Solo puede devolver `2`, `4`, `6`, `8` o `10`.

**Diferencia importante:**

```python
random.randint(1, 10)   # Incluye el 10
random.randrange(1, 10) # No incluye el 10
```

## 3.3 `random()` — Decimal entre 0 y 1

Devuelve un número decimal (`float`) mayor o igual que 0 y menor que 1.

**Sintaxis:**

```python
random.random()
```

**Ejemplo:**

```python
import random

decimal = random.random()
print(decimal)
```

Un resultado posible sería `0.734829...`.

No se le indican límites: devuelve un decimal en el intervalo `[0.0, 1.0)`.

## 3.4 `uniform(a, b)` — Decimal entre dos límites

Devuelve un número decimal aleatorio entre `a` y `b`.

**Sintaxis:**

```python
random.uniform(inicio, final)
```

**Ejemplo:**

```python
import random

precio = random.uniform(1, 10)
print(precio)
```

Puede devolver, por ejemplo, `4.7382`.

A diferencia de `randint()`, devuelve un decimal (`float`), no necesariamente un entero.

## 3.5 `choice(secuencia)` — Elegir un elemento

Selecciona **un único elemento** al azar de una secuencia, como una lista o una tupla.

**Sintaxis:**

```python
random.choice(secuencia)
```

**Ejemplo con una lista:**

```python
import random

nombres = ["Ana", "Luis", "Marta", "Pedro"]

elegido = random.choice(nombres)
print(elegido)
```

Devuelve uno de los nombres de la lista.

También se puede utilizar con una tupla:

```python
colores = ("rojo", "azul", "verde")
print(random.choice(colores))
```

**Importante:** la secuencia no puede estar vacía; si lo está, se produce un error (`IndexError`).

## 3.6 `choices(secuencia, k=n)` — Elegir varios elementos permitiendo repetición

Selecciona varios elementos al azar y devuelve una **lista**. Un mismo elemento puede salir más de una vez.

**Sintaxis:**

```python
random.choices(secuencia, k=cantidad)
```

- `secuencia`: lista, tupla u otra secuencia.
- `k`: cantidad de selecciones que queremos realizar.

**Ejemplo:**

```python
import random

nombres = ["Ana", "Luis", "Marta"]

elegidos = random.choices(nombres, k=5)
print(elegidos)
```

Podría devolver:

```text
['Ana', 'Marta', 'Ana', 'Luis', 'Ana']
```

Ana aparece varias veces porque `choices()` permite repetir elementos.

## 3.7 `sample(secuencia, k=n)` — Elegir varios elementos sin repetición

Selecciona `k` elementos diferentes de una población y devuelve una **lista**. No repite elementos.

**Sintaxis:**

```python
random.sample(secuencia, cantidad)
```

**Ejemplo:**

```python
import random

numeros = [1, 2, 3, 4, 5, 6]

elegidos = random.sample(numeros, 3)
print(elegidos)
```

Un resultado posible:

```text
[5, 2, 6]
```

No se repite ningún elemento.

**Importante:** la cantidad solicitada no puede ser mayor que el número de elementos disponibles.

## 3.8 `shuffle(lista)` — Mezclar una lista

Cambia el orden de los elementos de una lista de forma aleatoria.

**Sintaxis:**

```python
random.shuffle(lista)
```

**Ejemplo:**

```python
import random

cartas = ["As", "Rey", "Sota", " caballo"]

random.shuffle(cartas)

print(cartas)
```

El orden de la lista cambia aleatoriamente.

**MUY IMPORTANTE:**

- `shuffle()` modifica la lista original.
- No devuelve una nueva lista: su resultado es `None`.
- Se utiliza con listas, no directamente con tuplas o cadenas.

No hagas esto si quieres guardar el resultado:

```python
cartas = random.shuffle(cartas)  # Incorrecto: cartas pasa a valer None
```

Lo correcto es:

```python
random.shuffle(cartas)
print(cartas)
```

## 3.9 `seed(valor)` — Fijar la secuencia aleatoria

Permite iniciar el generador con una semilla. Si se utiliza la misma semilla y se repite la misma secuencia de operaciones, se obtienen los mismos resultados pseudoaleatorios.

**Sintaxis:**

```python
random.seed(valor)
```

**Ejemplo:**

```python
import random

random.seed(10)
print(random.randint(1, 100))
print(random.randint(1, 100))
```

Sirve especialmente para poder repetir pruebas y comprobar programas.

No se suele necesitar para los ejercicios normales de sorteos.

---

# 4. Otras funciones del módulo `random`

Estas funciones existen, aunque algunas son más avanzadas y no suelen ser necesarias en los primeros ejercicios.

| Función | ¿Para qué sirve? |
|---|---|
| `getrandbits(k)` | Devuelve un entero formado usando `k` bits aleatorios. |
| `triangular(a, b, modo)` | Devuelve un decimal siguiendo una distribución triangular. |
| `betavariate(alpha, beta)` | Genera un decimal con distribución beta. |
| `expovariate(lambd)` | Genera un decimal con distribución exponencial. |
| `gammavariate(alpha, beta)` | Genera un decimal con distribución gamma. |
| `gauss(mu, sigma)` | Genera un decimal con distribución normal. |
| `lognormvariate(mu, sigma)` | Genera un decimal con distribución log-normal. |
| `normalvariate(mu, sigma)` | Genera un decimal con distribución normal. |
| `vonmisesvariate(mu, kappa)` | Genera un ángulo con distribución de von Mises. |
| `paretovariate(alpha)` | Genera un decimal con distribución de Pareto. |
| `weibullvariate(alpha, beta)` | Genera un decimal con distribución de Weibull. |

Para empezar, céntrate sobre todo en `randint`, `randrange`, `random`, `uniform`, `choice`, `choices`, `sample` y `shuffle`.

---

# 5. Diferencias que pueden preguntar en un examen

| Función | Resultado | ¿Puede repetir? | ¿Modifica la colección original? |
|---|---|---|---|
| `randint(a, b)` | Un entero | No aplica | No |
| `randrange(a, b)` | Un entero | No aplica | No |
| `random()` | Un decimal | No aplica | No |
| `uniform(a, b)` | Un decimal | No aplica | No |
| `choice(lista)` | Un elemento | Una llamada elige uno | No |
| `choices(lista, k=...)` | Una lista | Sí | No |
| `sample(lista, k=...)` | Una lista | No | No |
| `shuffle(lista)` | `None` | Reordena los elementos | **Sí** |

## `choice()` frente a `choices()` y `sample()`

- `choice(lista)`: elige un elemento.
- `choices(lista, k=3)`: elige tres elementos y permite que se repitan.
- `sample(lista, 3)`: elige tres elementos diferentes, sin repetir.

## `sample()` frente a `shuffle()`

- `sample(lista, 3)`: devuelve una nueva lista con tres elementos seleccionados; no cambia la lista original.
- `shuffle(lista)`: mezcla todos los elementos de la lista original; la modifica directamente.

---

# 6. Ejemplo completo: sorteo de nombres

```python
import random

participantes = ["Ana", "Luis", "Marta", "Pedro", "Lucia"]

# Elegir una persona ganadora
ganador = random.choice(participantes)
print("GANADOR:", ganador)

# Elegir tres personas sin repetir
finalistas = random.sample(participantes, 3)
print("FINALISTAS:", finalistas)

# Elegir tres personas permitiendo que se repitan
seleccion = random.choices(participantes, k=3)
print("SELECCIÓN:", seleccion)

# Mezclar el orden de los participantes
random.shuffle(participantes)
print("LISTA MEZCLADA:", participantes)
```

Los resultados pueden cambiar en cada ejecución, porque las selecciones son aleatorias.

---

# 7. Errores habituales

1. **Confundir `randint()` con `randrange()`:** `randint(1, 10)` incluye el 10; `randrange(1, 10)` no lo incluye.
2. **Pensar que `random()` devuelve un entero:** devuelve un decimal entre 0.0 (incluido) y 1.0 (sin incluir).
3. **Confundir `choice()` con `choices()`:** `choice()` elige uno; `choices()` permite elegir varios y repetir.
4. **Pensar que `sample()` permite repetir:** no repite elementos.
5. **Guardar el resultado de `shuffle()`:** no devuelve la lista mezclada, sino `None`; modifica la lista original.
6. **Pedir más elementos de los disponibles con `sample()`:** produce un error.
7. **Utilizar `choice()` con una secuencia vacía:** produce un error.

---

# 8. Chuleta rápida

```python
import random

# ENTERO ENTRE 1 Y 10, INCLUYENDO AMBOS
random.randint(1, 10)

# ENTERO ENTRE 1 Y 9, SIN INCLUIR EL 10
random.randrange(1, 10)

# DECIMAL ENTRE 0 Y 1
random.random()

# DECIMAL ENTRE 1 Y 10
random.uniform(1, 10)

# ELEGIR UN ELEMENTO
random.choice(lista)

# ELEGIR VARIOS, PERMITIENDO REPETICIONES
random.choices(lista, k=3)

# ELEGIR VARIOS SIN REPETICIONES
random.sample(lista, 3)

# MEZCLAR LA LISTA ORIGINAL
random.shuffle(lista)

# FIJAR LA SEMILLA
random.seed(10)
```

**Lo más importante para el examen:** saber qué devuelve cada función, si permite repeticiones y si modifica la lista original.
