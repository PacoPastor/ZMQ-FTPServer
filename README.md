# Sistemas Distribuidos - Segunda Entrega
____


####Opción escogida: Transferencia de archivos

Para este proyecto hemos realizado una conexión cliente-servidor a partir de la tecnología ZeroMQ, en la cual el cliente dispondrá de una serie de opciones dadas por el servidor, de las cuáles el cliente escribirá una serie de instrucciones y el servidor devolverá la solicitud propuesta. Esta conexión será punto a punto y el cliente se conectará al único servidor a través del único puerto que se habilitará.

En nuestra opción elegida, definimos una serie de instrucciones, para el correcto manejo de archivos en el servidor a través de las instrucciones dadas en el cliente, como son:
  - Listar y  visualizar los archivos que se encuentran en la misma carpeta que el servidor
  - Copiar los ficheros a cualquier otra carpeta del servidor, inclusive donde se encuentre el fichero de ejecución del servidor
  - Mover los ficheros a cualquier otra carpeta del servidor, inclusive donde se encuentre el fichero de ejecución del servidor
  - Eliminar los ficheros de la carpeta del servidor

---

####Integrantes
 - Francisco José Pastor Aznar
 - Alejandro Chacón Peregrino
 - Antonio Rafael Gambín Íñigo
 - Iván Ruíz Valle
 
____
####Variantes del Proyecto
Al ser el último proyecto de la asignatura, y con la correcta preparación para abordar el problema que nos conscierne, realizamos la resolución del problema de una forma local, pero gracias a la versatilidad de la arquitectura y simpleza de la arquitectura efectuada, hicimos otra versión de carácter remota.

Es decir, permitimos la consulta completa de forma local, que era nuestro proyecto inicial, y además, conseguimos listar los ficheros de una máquina remota.

___
####Ejecución
Para la ejecución, primero deberemos de instalar los paquetes necesarios, así:
- Si nos encontramos en un sistema basado en *Debian*, deberemos de tener instalado el gestor de módulos de aplicaciones de terceros en Python **pip** y en una terminal, escribir
```sh
$ pip install pyzmq
```
- Si nos encontramos en otros sistemas, como puede ser Arch Linux, podremos instalarlo de una forma más sencilla como es:
```sh
$ yaourt python2-pyzmq
```

Una vez instalado las dependencias, pasamos a la ejecución de las instrucciones. Así, para la ejecución de la variante local, sería:
```sh
$ python2.7 clienteftp
```
```sh
$ python2.7 serverftp
```

y para la ejecución de la variante remota, sería:
```sh
$ python2.7 clienteftp[IP]
```
```sh
$ python2.7 serverftp
```
____
##Recursos
- ***Campus de Sistemas Distribuido:*** https://www.uca.es
- ***Aprendiendo ZeroMQ:*** http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/
