"""
DIFERENCIAS CON OTROS LENGUAJES QUE HEMOS VISTO:
- NO HAY FUNCIÓN MAIN OBLIGATORIA
- TIPADO DINÁMICO
- SANGRÍA EN VEZ DE LLAVES
"""

print("Picha") # pa printear

# variables
# nombre = valor

nombre = "Daniel"
nota = 9.8
seximetro = 120
listo = True

# if

if True:
    print("Esto se ejecuta")
else:
    print("Esto no")

# ELSE OPCIONAL

# BUCLES
# NO HAY FOR CLÁSICO
# POR DEFECTO ES FOREACH
# Y PA TENER UNA VARIABLE QUE SE VAYA INCREMENTANDO SE USA `range`

# se puede poner dónde acaba y va de 0 hasta n - 1 yendo de 1 en 1
for i in range(10): # de 0 a 9
    print(i)

# se puede poner dónde empieza
for i in range(20, 50): # 20 a 49
    print(i)

# también salto
for i in range(10, 101, 10): # 10 a 100 de 10 en 10
   print(i)

# EL WHILE ES NORMAL
while True:
    print("Infinito a menos que haya:")
    break

# FUNCIONES
# def nombre():
#   ...

def nota(alumno):
    if alumno == "Daniel":
        return 9.8

    return 5

print(nota("Daniel"))
print(nota("Jesús"))


# COLECCIONES
# OBJETOS PA TENER EN UN SÓLO SITIO VARIAS COSAS

# LISTAS
gente_guay = [
    "Marta",
    "Daniel",
    "Jesús",
    "Samuel"
]

for nombre in gente_guay:
    print(nombre)

"""
Se pueden iterar:
- Cualquier colección
- Generadores como el range
- Strings (caracter a caracter)
"""

# tuplas
# LISTA INMUTABLE

gente_guay.append("Anvest")

notas_de_daniel = (9.2, 9.8, 10)

# diccionario
# como el mapa de java y kotlin y lo que te dé la gana
# clave valor

notas_pichon = {
    "Daniel": 9.8,
    "Samuel": 9.9,
    "Marta": 10,
    "Jesús": 9.7
}

notas_pichon["Anvest"] = 15
print(notas_pichon["Anvest"])
print(notas_pichon)

# Da las claves
for alumno in notas_pichon:
    print(alumno)

# Da clave y valor
for alumno, nota in notas_pichon.items():
    print(f"{alumno}: {nota}")

# set
# lista con 2 diferencias
# no admite valores duplicados
# no está ordenada

gente_que_me_cae_mal = {"Jesús", "Alejandro"}

print(gente_que_me_cae_mal)
gente_que_me_cae_mal.add("Jesús")
print(gente_que_me_cae_mal)

# TODO: {} = dict, set() para set vacío



# FUNCIONES DE ORDEN SUPERIOR
