Tecnologias utilizadas:
Python 3.15.2
Django 6.1.2
Bootstrap 

Para instalar las dependencias utilizar el siguiente comando despues de moverse a la carpeta donde se encuentra el proyecto y el archivo "requirements.txt" y haber instalado python de su pagina oficial siguiendo las especificaciones y descargando cualquier version 3.x

pip install -r requirements.txt

--------------------------------------------------------

para configurar la base de datos primero debera acceder a la pagina al buscar en un navegador de preferencia al empezar a correr el servidor

comando para correr el servidor dentro de la carpeta donde se encuentra manage.py:
py manage.py runserver

posteriormente ingrese lo siguiente en su navegador:
http://127.0.0.1:8000/

con ese link accedera a la pagina web, para acceder a la base de datos en si ingrese:
http://127.0.0.1:8000/admin

dentro los datos son:
usuario: admin
contraseña: admin123

ya en la interfaz vera la seccion "autenticacion y autorizacion" donde podra añadir grupos o usuarios de manera manual, al igual que asignar al staff al editar alguno de los usuarios existentes o añadirlo directamente.
La sección "Patrimonio" presenta las categorias y LugarPatrimonial (tenga en cuenta que LugarPatrimonial es editable por el staff dentro de gestion desde la pagina principal sin tener que acceder a http://127.0.0.1:8000/admin al iniciar sesion con su cuenta de staff)

al dar click en modificar se encontrara con el nombre de la categoria, nombre de usuario, nombre de grupo, nombre de lugar patrimonial que estan ya en la base de datos, para añadir uno arriba a la derecha se encuentra el boton para añadir y siguiendo las indicaciones podra añadir alguno de los deseados o modificar algun parametro