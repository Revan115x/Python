"""Apartados:
1. Muestra el nombre del usuario.
2. Muestra su edad.
3. Cambia su ciudad a "Barcelona".
4. Añade una nueva clave "email" con el valor "carlos@gmail.com".
5. Modifica su edad sumándole 1.
6. Elimina la clave "activo".
7. Muestra el diccionario completo.

CREAR · CONSULTAR · MODIFICAR · ELIMINAR"""

usuario = {
    "nombre": "Carlos",
    "edad": 22,
    "ciudad": "Madrid",
    "activo": True
}

print(usuario.get("nombre"))
print(usuario.get("edad"))
usuario["ciudad"] = "Barcelona"
usuario["email"] = "carlos@gmail.com"
usuario["edad"] += 1
print(usuario.get("ciudad"))
usuario.pop("activo")

print(usuario)