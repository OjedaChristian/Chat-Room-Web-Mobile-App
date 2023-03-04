<div align="center">
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/home.png">

# Aplicación "Chat-Room" para Web y Móvil - Proyecto Backend con Django
</div>

Está aplicación nos permite crear salas independientes con temáticas exclusivas a las que pueden acceder otros usuarios, unirse y comentar sobre dicho tema, es un pequeño proyecto enfocado a aplicar nuevos conocimientos con Python/Django enfocados a backend.

En el proyecto se ha utilizado Python, con el framework Django, junto con HTML, CSS, JavaScript.
<br>

## Características de la app

* Autenticación / Registro de usuarios.
* User model personalizado e integración.
* Restricción a usuarios.
* Mensajería Flash.
* Operaciones CRUD.
* Sistema de creación de salas personalizadas para cada temática.
* Sistema de búsqueda / filtrado avanzado por temática, nombre coincidente.
* Creación de Middleware personalizado que muestra diferentes datos del usuario en la consola del servidor.
* Creación y personalización de Forms.
* Sistema de perfiles de usuario y configuración / personalización de los mismos.
* Sistema de seguimiento de actividad (mensajes) de los usuarios en las salas.
* Implementación de Static files (js, css, imágenes).
* Instalación de "Templates" externas y vinculación con el backend.
* Adaptación de la app según el dispositivo, apto para móvil y web.
* REST Framework - se ha creado una API básica que muestra datos de todas las salas creadas en la app, a las que podemos acceder individualmente y ver sus     propiedades.

## CHAT ROOM - PREVISUALIZACIÓN DEL PROYECTO

<div align="center">
<p>
<br>
  <strong>Inicio web</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/home.png"/>
<p>
<br>
<p>
<br>
  <strong>Inicio mobile</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/home_mobile.png"/>
<p>
<br>
  <strong>Inicio de sesión web</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/login.png"/>
<p>
<br>
  <strong>Inicio de sesión mobile</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/login_mobile.png"/>
<p>
<br>
<p>
<br>
  <strong>Registro web</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/register.png"/>
<p>
<br>
  <strong>Registro mobile</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/register_mobile.png"/>
<p>
<br>
  <strong>Búsqueda salas web</strong>
</p>
<br>
<img width="50%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/searchbar.png"/>
<p>
<br>
  <strong>Búsqueda salas avanzada </strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/search_advanced.png"/>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/search_advanced2.png"/>
<p>
<br>
  <strong>Búsqueda salas avanzada mobile</strong>
</p>
<br>
<img width="30%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/search_advanced_mobile.png"/>
<p>
<br>
  <strong>Perfiles de usuario</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/user_profile.png"/>
 <img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/user_profile2.png"/>
<p>
<br>
  <strong>Perfiles de usuario mobile</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/user_profile_mobile.png"/>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/user_profile_mobile2.png"/>
<p>
<br>
  <strong>Menú de actividad de usuarios mobile</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/activity_mobile.png"/>
<p>
<br>
  <strong>Creación de salas</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/create_room.png"/>
<img width="100%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/create_room2.png"/>
<p>
<br>
  <strong>Salas web</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/pc_room.png"/>
<p>
<br>
  <strong>Salas mobile</strong>
</p>
<br>
<img width="30%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/mobile_room.png"/>
<p>
<br>
  <strong>Filtrado de salas por temática</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App/blob/main/.github/filtro.png"/>
</div>

## Instalación

### Clona el repositorio

--> Para clonar el repositorio deberá tener instalado Git, compruébelo :
```bash
git --version
```

Puede instalar Git desde: https://www.geeksforgeeks.org/how-to-install-git-on-windows-command-line/

--> Clone el repositorio utilizando el siguiente comando :
```bash
git clone https://github.com/OjedaChristian/Chat-Room-Web-Mobile-App.git
```


--> Muévase al directorio dónde haya clonado el proyecto : 
```bash
cd Chat-Room-Web-Mobile-App
```

--> Crea un entorno virtual para el proyecto :
```bash
# Instalamos virtualenv
pip install virtualenv
# Creamos el entorno virtual
py -m venv envchatroom
```

--> Activamos el entorno virtual creado :
```bash
envchatroom\Scripts\activate
```

--> Instalamos los requisitos del proyecto de forma local en el entorno virtual :
```bash
pip install -r requirements.txt
```

#

### Inicializamos la aplicación

--> Inicializamos el servidor :
```bash
python manage.py runserver
```

> ⚠ Utilizaremos la url que nos provee para acceder a la app desde cualquier navegador web: http://127.0.0.1:8000/
> ¡Ya puede utilizar el proyecto desde su propio equipo y probar todas sus características!
#
## Autor

Christian Ojeda
