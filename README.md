# Titulo del proyecto

Las principales características del proyecto incluirán:

Registro e inicio de sesión de usuarios.
Visualización de una biblioteca de libros con reseñas y calificaciones.
Creación, edición y eliminación de reseñas de libros por parte de los usuarios.
Seguimiento de autores favoritos por parte de los usuarios.
Filtros para buscar libros por género y autor.
Administración del sistema por parte de los administradores, incluida la gestión de usuarios, libros y reseñas.

## Descripción del proyecto

LibrosPlus es una aplicación web desarrollada en Django que ofrece a los usuarios la posibilidad de registrarse, acceder a sus cuentas, compartir libros, escribir reseñas, filtrar obras y valorar el trabajo de diferentes autores. Este proyecto cuenta con un sistema de autenticación único y permite a los usuarios tanto añadir como explorar una amplia variedad de libros.

## Capturas de Pantalla del Proyecto

Incluir capturas de pantalla o imágenes que muestren el proyecto en funcionamiento.

![Home](imagenes/home.png)
Vista inicio de la aplicación.

## Configuración del proyecto

Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

- Sistema Operativo Ubuntu 20.04, Windows 10
- Python 3.8
- Django 4.2.11
- PostgreSQL

## Instalación del Proyecto

1. Clonar el repositorio:

   ```ssh
   git@github.com:gonliv/librosEmpresa.git

2. Crear y activar un entorno virtual:

    python -m venv env
    # En Linux / WSL usar
    source env/bin/activate  

3. Instalar las dependencias:

    pip install -r requirements.txt

4. Configurar la base de datos PostgreSQL en settings.py:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "resena_libross",
            "USER": "tu_usuario",
            "PASSWORD": "tu_pw",
            "HOST": "127.0.0.1",
            "PORT": "tu_puerto",
        }
}

## Instrucciones para Ejecutar el Proyecto

Instrucciones para ejecutar el proyecto una vez instalado.

```bash
#
```

## Instrucciones para Cargar los Datos Semilla a la Base de Datos

Comandos necesario para cargar los datos semilla a la base de datos.

```bash
python manage.py loaddata seed_data.json
```

## Credenciales de Acceso

### Para Usuario Tipo Administrador

- Email: administrador@mail.com
- Contraseña: Abc123#

### Para Usuario Tipo Reader

- Email: lector@mail.com
- Contraseña: Abc123#

## Autor

- [Gonzalo Olivares C](https://github.com/gonliv)

## Licencia

Este proyecto está bajo la Licencia MIT - ve el archivo [LICENSE.md](LICENSE) para detalles.