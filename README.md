<div align="center">
<img width="100%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/home.png">

# Aplicación "Chat-Room" para Web y Móvil - Proyecto Backend con Django
</div>

Está aplicación nos permite crear salas independientes con temáticas exclusivas a las que pueden acceder otros usuarios, unirse y comentar sobre dicho tema, es un pequeño proyecto enfocado a aplicar nuevos conocimientos con Python/Django enfocados a backend.

En el proyecto se ha utilizado Python, con el framework Django, junto con HTML, CSS, JavaScript.
<br>

## Características de la app

* Autenticación / Registro de usuarios
* User model personalizado.
* Restricción a usuarios.
* Mensajería Flash.
* Operaciones CRUD.
* Sistema de búsqueda/filtrado avanzado por temática, nombre coincidente.
* Creación de Middleware personalizado que muestra diferentes datos del usuario en la consola del servidor.
* Creación y personalización de Forms.
* Sistema de perfiles de usuario y modificación de los mismos.

* Instalación de "Templates" externas y vinculación con el backend.
* REST Framework - se ha creado una API básica que muestra datos de todas las salas creadas en la app, a las que podemos acceder individualmente y ver sus     propiedades.

  * Subida de imágenes / contenido a la app
      * Subida de imágenes:
          * Título
          * Descripción
          * Autor / Usuario
          * Fecha de subida de la imagen
          * Sistema de Likes (Podrás dar/quitar likes a cualquier publicación con diferentes usuarios y acumular dichos likes)
          * Descarga de imágenes de la app (Puedes descargar cualquier imagen subida mediante un botón)

* Configuración del perfil de usuario
  * El usuario podrá añadir o modificar estas opciones para que aparezcan en su perfil de usuario.
    * Nombre de usuario
    * Imagen de perfil
    * Banner del perfil
    * Biografía / Sobre mí
    * Localización
    * Empleo actual dentro del sector
    * Especialización (Ilustrador, artista 3D, etc...)
    * Website / Portfolio del artista
    * Email de contacto
    
* Búsqueda de usuarios / barra de búsqueda por nombre de usuario    
* Perfil de usuario
  * Los usuarios podrán encontrar tú perfil buscando por tú usuario o mediante el sistema de sugerencia de usuarios, en tú perfil aparecerán los siguientes      datos:
    * Usuario - Email del usuario
    * Biografía
    * Número de usuarios a los que sigues
    * Número de seguidores
    * Número de imágenes subidas
    * Acceso / visualiación de todas las imágenes subidas por el usuario

* Sistema de seguimiento de usuarios
   * Podrás seguir / dejar de seguir usuarios, esto afectará a tu inicio / feed y mostrará imagénes subidas por usuarios a los que sigues, además si accedes a tú perfil no podrás seguirte, aparecerá 'configurar mi perfil' y te permitirá cambiar opciones de tu perfil.
    * Botón dinámico seguir / dejar de seguir / configurar mi perfil
    
* Explorar /  sistema de filtrado de imágenes mediante combinación de parámetros
  * Al acceder a 'Explorar' podrás buscar y filtrar todas las imágenes subidas a la app, las opciones del sistema de filtro son las siguientes:
    * Filtro por género de la imagen (Ilustración, fantasía, arte conceptual, paisajes, retratos, diseño)
    * Filtro por usuario / autor de la obra
  

## ARTBOOK - PREVISUALIZACIÓN DEL PROYECTO

<div align="center">
<p>
<br>
  <strong>Registro de usuarios</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/signup.png"/>
<p>
<br>
  <strong>Inicio de sesión</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/signin.png"/>
<p>
<br>
  <strong>Home / Feed</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/home.png"/>
<p>
<br>
  <strong>Subida de imágenes</strong>
</p>
<br>
<img width="50%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/Upload.png"/>
<p>
<br>
  <strong>Búsqueda de usuarios</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/search.png"/>
<p>
<br>
  <strong>Menú perfil del usuario activo</strong>
</p>
<br>
<img width="30%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/perfil.png"/>
<p>
<br>
  <strong>Perfil del usuario activo</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/perfil2.png"/>
<p>
<br>
  <strong>Configuración de perfil del usuario activo</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/perfil3.png"/>
<p>
<br>
  <strong>Visitando el perfil de otros usuarios de la app</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/perfil5.png"/>
<p>
<br>
  <strong>Visualizamos las imágenes subidas por otros usuarios desde su perfil</strong>
</p>
<br>
<img width="100%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/perfil4.png"/>
<p>
<br>
  <strong>Exploramos las imágenes subidas en la app / filtramos por imágenes catalogadas como 'Ilustraciones' </strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/explore.png"/>
<p>
<br>
  <strong>Filtramos ahora imágenes catalogadas como 'Retratos' </strong>
</p>
<br>
<img width="30%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/explore2.png"/>
<p>
<br>
  <strong>Vemos los resultados obtenidos</strong>
</p>
<br>
<img width="70%" src="https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas/blob/main/.github/explore3.png"/>
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
git clone https://github.com/OjedaChristian/ARTBOOK---Red-Social-para-artistas.git
```

--> Muévase al directorio dónde haya clonado el proyecto : 
```bash
cd ARTBOOK---Red-Social-para-artistas
```

--> Crea un entorno virtual para el proyecto :
```bash
# Instalamos virtualenv
pip install virtualenv
# Creamos el entorno virtual
py -m venv envartbook
```

--> Activamos el entorno virtual creado :
```bash
envartbook\Scripts\activate
```

--> Instalamos los requisitos del proyecto en el entorno virtual :
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
