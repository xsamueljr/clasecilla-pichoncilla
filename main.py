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
    "Franmi",
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

# ADVERTENCIA SI QUIERES CREAR UN SET VACÍO

# mmm qué listo soy los sets son con llaves así que pongo llaves sin nada
print(type({})) # DA DICT

print(type(set())) # esto sí es un set


# FUNCIONES DE ORDEN SUPERIOR
# PARA APLICAR UNA FUNCIÓN A UNA COLECCIÓN Y NO HACER BUCLES
# OMG PROGRAMACIÓN FUNCIONAL SÍ OH OH OH YES DIDDY

"""
- map: Aplica una función a cada elemento y te crea una colección nueva con lo que devuelve
- filter: Aplica una función que devuelve un booleano y te devuelve una colección con los que devuelvan verdadero
"""

def cuadrado(x):
    return x ** 2

ejemplos = list(range(1, 11))
cuadrados = list(map(cuadrado, ejemplos))
print(cuadrados)

# COSAS DE PROCESOS
from functools import wraps
import subprocess
import time

ls_result = subprocess.run(["ls", "iuiagdfiuyg"], capture_output=True, text=True)
print("Salida estándar: " + ls_result.stdout)
print("Error estándar: " + ls_result.stderr)

python_subprocess = subprocess.Popen(
    ["uv", "run", "python"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

salida, error = python_subprocess.communicate(input="print('algo')")
print(salida)
print(error)

"""
run espera a que el proceso termine
Popen sólo lo crea y te vuelve a pasar el control

Si el programa va a terminar sin pedir nada y quieres lo que te devuelve y ya, run
y si quieres su resultado inmediatamente

Popen si tu programa y el que invocas van a convivir de alguna forma (comunicarse con communicate)
o pueden trabajar en paralelo (tu programa hace otra cosa mientras)

"""

mayusculator_process = subprocess.Popen(
    ["uv", "run", "python", "-c", "print(input().upper())"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True
)

en_mayusculas, _ = mayusculator_process.communicate(input="algoritmos")
print(en_mayusculas)

# invocar, esperar y matar
notepad_process = subprocess.Popen(["gnome-text-editor"])

time.sleep(3)

notepad_process.terminate()

# invocar, monitorear, y mirar código de salida

notepad_process = subprocess.Popen(["gnome-text-editor"])

while notepad_process.poll() is None:
    time.sleep(1)
    print("El notepad sigue abierto")

print(f"Código de salida: {notepad_process.poll()}")

procesos = []

procesos.append(subprocess.Popen(["gnome-text-editor"]))
procesos.append(subprocess.Popen(["gnome-calculator"]))

for proceso in procesos:
    while proceso.poll() is None:
        time.sleep(1)

for proceso in procesos:
    print(f"Código de salida del proceso {proceso.pid}: {proceso.poll()}")

# DECORADORES
# Función que le mete funcionalidad a otra

def medir_tiempo(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        difference = end - start
        print(f"La función ha tardado {difference:.2f} segundos")
    return envoltura

@medir_tiempo
def funcion_lenta():
    time.sleep(1)


funcion_lenta()
