Gunicorn usa el puerto 8000.

El archivo nginx_app.conf configura NGINX como proxy inverso,
redirigiendo las peticiones al servicio Flask.

Los logs se escriben en el archivo logs/app.log.

wsgi.py es el punto de entrada de la aplicación para Gunicorn.
