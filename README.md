# Multithreading vs Multiprocessing vs Async

## Concurrencia y Paralelismo
- Concurrencia: Hacer muchas cosas juntas ejm: 
    + Pepito esta preparando su desayuno y mirando Youtube.

- Paralelismo: hacer muchas cosas al mismo tiempo. ejm: 
    + pepito programa y zulema està haciendo tik tok.

## Proceso: 
+ Es un programa o fragmento de programa en ejecuciòn.

Todo proceso creado necesita una serie de recursos (paquete de informacion, BCP), el cual se los brinda el SO (espacio de memoria y tiempo de uso, etc)

![](/images/bloqueControl.png)

- Planificador de Procesos: Tiene funciones (decidir què proceso utilizar, y cuadno un proceso puede pasar a otro estado, etc)y objetivos del SO.
    * Equidad, Eficiencia, tiempo de respuesta bajo, Alto rendimiento; ayudado de un algoritmo de planificacipon (FIFO, RUEDA (Round-Robin), RR (Prioridad Circular, SJF (primera tarea mas corta))
Gracias a la tècnica de la multiprogramaciòn nos permite que dos o mas procesos se puedan ejecutar "a la vez" (concurrencia de procesos)

De todos los procesos que se estàn ejecutando, solo 1 tiene la "atenciòn del usuario", este proceso estarà en __primer plano__, el resto en __segundo plano__

### Cambio de contexto
![](/images/ASIR_ISO01_CONT_R11_cambiocontexto.png)

### Estados de Procesos

![](/images/precesosEstados.png)


### Hilo:  Es la parte de un proceso que puede ser ejecutada de forma independiente, Instancia dentro de un proceso. Secuencia de intrucciones dentro de proceso.

De esta manera, un proceso estarà constituido por al menos 1 hilo, existiendo la posibilidad de que tenga varios.

+ Multihilo: capacidad del SO de mantener varios hilos en ejecuciòn dentro de un mismo proceso, 


![](/images/hilos.png)


Multiprocessing: Se refiere a un sistema que __tiene màs de 2 unidades centras de procesamiento__. Esto permite ejecutar varios proceso en simultàneo.


## Hablemos de Python

## MultiThreading: Mòdulo Threading que permite lanzar hilos y controlarlos
+ En CPython(el oficial) no soporta paralelismo real
+ en otros python SÌ(N cores)
+ En casos de muchas tareas (hilos), o esperas I/O muy largas, el context switch hace que no sea tan eficiente.

`subprocess`: proporciona una interfaz para crear y comunicarse con procesos secundarios. 
`signal`: espone el mecanismo de señal de Unix para enviar eventos a otros procesos. señales se procesan de forma asincroma.
`threading` incluye una interfz de alto nivel orientada a objetos.

https://ikastaroak.birt.eus/edu/argitalpen/backupa/20200331/1920k/es/ASIR/ISO/ISO01/es_ASIR_ISO01_Contenidos/website_312_procesos.html

https://www.youtube.com/watch?v=u77Az26bFPA

https://es.acervolima.com/multithreading-en-python-serie-1/


