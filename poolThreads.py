# Que es: mecanismo que nos permite crear n cantidad de thread que nos da la posibilidad 
# de reciclar thread y asignar nuevas tareas
import time
import logging

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-s%(message)s)')

def super_task(a,b):
    for i in range(a,b):
        print(i)
        time.sleep(1)
    logging.info(f": hacemos un for de {a} - {b} con sleep de 1 segundo!!!")
    return 

if __name__ == '__main__':
    
    executor = ThreadPoolExecutor(max_workers=2)

    executor.submit(super_task, 1, 4)
    executor.submit(super_task, 2, 5)
    executor.submit(super_task, 3, 6)
    executor.submit(super_task, 4, 7)
