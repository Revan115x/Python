"""6. Escribir un programa que cree un diccionario de traducción español-
inglés. El usuario introducirá las palabras en español y su traducción al

inglés. Después pedirá una frase en español y utilizará el diccionario para
traducirla palabra a palabra. Si una palabra no está en el diccionario debe
dejarla sin traducir."""

traducciones = {
    "hola": "hello",
    "casa": "house",
    "perro": "dog",
    "gato": "cat"
}

espanol=input("PALABRA EN ESPAÑOL :")

espanol=espanol.lower();


if espanol in traducciones:
    print("Traduccion ", traducciones[espanol] )
else:
    print("NO TENEMOS TRADUCCION")


ingles=input("PALABRA EN ingles :")

ingles=ingles.lower();

for espanol, ingles_dic in traducciones.items():
    if ingles_dic == ingles:
        print("Traduccion:", espanol)