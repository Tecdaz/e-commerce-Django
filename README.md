# Django eCommerce

Este es un proyecto sencillo de eCommerce desarrollado con Django. El objetivo de esta aplicación es simular una tienda en línea donde los usuarios pueden explorar productos. El proyecto permite la creación de un catálogo de productos con detalles básicos como nombre, descripción y precio.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu máquina:

- Python 3.x
- pip (gestor de paquetes de Python)
- virtualenv (opcional pero recomendado)

## Instalación

Sigue los pasos a continuación para configurar el proyecto en tu entorno local.

### 1. Crear un entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto. Puedes crear un entorno virtual con el siguiente comando:

```bash
python -m venv env
```

### 2. Activar el entorno virtual

Activa el entorno virtual que acabas de crear.

- En sistemas **Windows**:
  
  ```bash
  .\env\Scripts\activate
  ```

- En **macOS/Linux**:

  ```bash
  source env/bin/activate
  ```

### 3. Instalar las dependencias

Una vez que el entorno virtual esté activado, instala las dependencias del proyecto usando el siguiente comando:

```bash
pip install -r requirements.txt
```

### 4. Migrar la base de datos

Crea las tablas necesarias para la base de datos ejecutando las migraciones:

```bash
python manage.py migrate
```

### 5. Poblar la base de datos

Ejecuta el script `populate.py` para cargar algunos productos de ejemplo en la base de datos:

```bash
python populate.py
```

### 6. Ejecutar el servidor

Finalmente, inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

El servidor se ejecutará en `http://127.0.0.1:8000/`. Abre tu navegador y visita esta URL para ver el proyecto en funcionamiento.

## Estructura del Proyecto

- **manage.py**: Script principal para interactuar con el proyecto Django.
- **requirements.txt**: Archivo que contiene las dependencias del proyecto.
- **populate.py**: Script para cargar productos de ejemplo en la base de datos.
- **app_name/**: Carpeta de la aplicación principal del eCommerce (puedes cambiarla por el nombre de tu app).

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

¡Gracias por usar este proyecto! 😊
