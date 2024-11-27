# fast-users

fast-users es una aplicación desarrollada con **FastAPI** para la gestión de usuarios. Proporciona endpoints **API REST** para realizar operaciones CRUD sobre usuarios almacenados en una base de datos PostgreSQL.

## Características
- **CRUD de Usuarios**: Crear, leer, actualizar y eliminar usuarios.
- **Paginación**: Consultar listas de usuarios con límites y desplazamientos.
- **Persistencia**: Almacena datos en una base de datos PostgreSQL.
- **External API**: Integra con una API externa para obtener datos.
- **Configuración modular**: Gestión centralizada de configuración con Pydantic Settings.
- **Logging**: Registro de eventos mediante archivos rotativos.

## Requisitos
    Python 3.10 o superior
    PostgreSQL

## Dependencias
El proyecto utiliza las siguientes dependencias principales:
**fastapi==0.115.2**: Framework principal para el desarrollo de la API.
**uvicorn==0.32.0**: Servidor ASGI para ejecutar la aplicación.
**pydantic[email]==2.9.2**: Validación de datos, incluyendo soporte para email.
**requests==2.32.3**: Para realizar peticiones a APIs externas.
**SQLAlchemy==2.0.36**: ORM para interactuar con la base de datos.
**psycopg2-binary==2.9.10**: Driver para conectar a PostgreSQL.
**alembic==1.13.3**: Herramienta para manejo de migraciones en la base de datos.
**pydantic-settings==2.6.0**: Carga y validación de configuraciones basadas en Pydantic.

## Puesta en marcha
1. Crear un entorno virtual y activarlo
    python -m venv venv
    source venv/bin/activate
2. Instalar dependencias del archivo `requirements.txt`
    pip install -r requirements.txt
3. Ejecutar con Python el archivo `main.py`
    python main.py o python3 main.py
4. Acceder a la documentacion interactiva en `/docs` o `/redoc`
    Swagger UI: http://127.0.0.0:8000/docs
    Redoc: http://127.0.0.0:8000/redoc
5. Configurar la base de datos
    Asegúrate de que el servidor PostgreSQL esté funcionando
    Ejecuta las migraciones iniciales: alembic upgrade head