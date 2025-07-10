# 🧾 Backend de Gestión de Citas de Entrega

Proyecto Django REST API para la gestión de citas de entrega, proveedores y reportes de tiempo promedio. Incluye autenticación, documentación interactiva y análisis de datos.

## Estructura del Proyecto
core/
    │
    ├── models/               # Modelos de base de datos
    ├── serializers/          # Serializers DRF
    ├── views/                # Vistas (APIViews)
    ├── services/             # Lógica de negocio
    ├── exceptions/           # Excepciones personalizadas
    ├── routers/              # Rutas por módulo
    ├── migrations/           # Archivos de migración


## 📖 Documentación
- [Documentación de la API](http://127.0.0.1:8000/docs/)

---

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

```env
DEBUG=True
SECRET_KEY='django-insecure-(i%2^%$o(ng^zm@ctq0hi_i-8cp$xb#!^5t@#x=zpmk$)e-5i^'
DB_NAME=sgc_db
DB_USER=lilo
DB_PASSWORD=sinverguenza
DB_HOST=localhost
DB_PORT=5432
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






