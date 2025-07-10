# 🧾 Backend de Gestión de Citas de Entrega

Proyecto Django REST API para la gestión de citas de entrega, proveedores y reportes de tiempo promedio. Incluye autenticación, documentación interactiva y análisis de datos.

## Estructura del Proyecto
```
core/
    │
    ├── models/               # Modelos de base de datos
    ├── serializers/          # Serializers DRF
    ├── views/                # Vistas (APIViews)
    ├── services/             # Lógica de negocio
    ├── exceptions/           # Excepciones personalizadas
    ├── routers/              # Rutas por módulo
    ├── migrations/           # Archivos de migración
```


## 📖 Documentación
- [Documentación de la API](http://127.0.0.1:8000/docs/)

---

## Esquema UML
![Imagen de WhatsApp 2025-07-10 a las 10 40 41_b2dc7a59](https://github.com/user-attachments/assets/5d4a8a33-ebb3-42ae-a4b4-cdf8c43690c6)


## 🚀 Requisitos

- Python 3.10+
- PostgreSQL
- pip o pipenv
- Entorno virtual (recomendado)

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```
### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Editar el archivo `.env`
Crea un archivo `.env` en la raíz del proyecto y configura las variables de entorno necesarias:

### Tener en cuenta que se debe crear la base de datos(Postgres) antes de correr las migracion y agregarlas en tu .Env

```env
DEBUG=True
SECRET_KEY='django-insecure-(i%2^%$o(ng^zm@ctq0hi_i-8cp$xb#!^5t@#x=zpmk$)e-5i^'
DB_NAME=****
DB_USER=***
DB_PASSWORD=******
DB_HOST=*****
DB_PORT=****
```

### 5. Migraciones de la base de datos

```bash
python manage.py migrate
```

### 6. Correr los datos fixtures
    
```bash
python manage.py loaddata core/fixtures/initial_data.json
```

### 7. Levantar el servidor

```bash
python manage.py runserver
```






