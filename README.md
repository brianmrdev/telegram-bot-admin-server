# Telegram-Bot-Admin-Server

Bot de Telegram para realiza acciones básicas en mi VPS como:

 - Iniciar, detener o reiniciar servicios utilizando **systemctl**.
 - Conocer que usuarios estan logueados en mi server, desde que IP y la hora que realizaron la conexion.
 - Conocer la fecha y hora desde cuando mi servidor esta online.
 - Consultar el uso del HDD, RAM y CPU.
 - Eliminar ficheros y carpetas en un directorio especifico que utilizo como ruta de descargas.

# Instalación

Pasos para poner en funcionamiento el bot

 1. Clonamos el repo:
  `git clone https://github.com/brianmrdev/telegram-bot-admin-server.git`
 2. Entramos al proyecto clonado, creamos el entorno virtual y lo activamos:
 `cd telegram-bot-admin-server`
 `python3 -m venv venv`
 `source venv/bin/activate`
 3. Instalamos los paquetes necesarios:
 4. `pip install -r equirements.txt`
 5. Y por último ajustamos los parametros que se encuentran en el fichero **config.py**