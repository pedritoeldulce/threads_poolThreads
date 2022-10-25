import time
import threading
import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-s%(message)s)')


def consulta(id_persona):
    logging.debug(f"consultado para el id {id_persona}")
    for i in range(1,8):
        print(i)
        time.sleep(1)
    return

def guardar(id_persona, data):
    logging.info(f"consultando para el id: {id_persona} data:{data}")
    for i in range(10, 15):
        print(i)
        time.sleep(1)
    return 

tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo_1", target=consulta, args=(1,))
t2 = threading.Thread(name="hilo_2", target=guardar, args=(1, "Nocanoa"))

t1.start()
t2.start()


t1.join() # Espera a que los hilos terminen de ejecutar, para luego procesar el hilo principal
t2.join()
""" consulta(1)
guardar(1, "Noacanoa") """
    
tiempo_fin = datetime.datetime.now()
print(f"Tiempo transcurrido: {tiempo_fin.second - tiempo_ini.second}" )

# Resultado
""" [DEBUG] (hilo_1consultado para el id 1)
1
[INFO] (hilo_2consultando para el id: 1 data:Nocanoa)
10
2
11
3
12
13
4
14
5
6
7
Tiempo transcurrido: 7 """