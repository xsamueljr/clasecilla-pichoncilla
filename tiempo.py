import time

# time.time() => Segundos desde el 1 de enero de 1970 (lol)
#
# si lo ejecutas una vez, pasan 2 segundos y lo vuelves a ejecutar,
# te dará más o menos lo de antes + 2
#
# entonces el proceso es el siguiente:
# 1. lo llamas una vez
# 2. haces lo que sea que quieras medir
# 3. lo llamas otra vez
# 4. restas el segundo menos el primero
#
# El resultado es los segundos de un momento a otro

start = time.time()
time.sleep(1)
end = time.time()

print(end - start) # 1 aprox, con decimales
