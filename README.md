# DonD' Lucho Backend

## Django
### 1. Instalar Python >= 3.10 e instalar virtualenv con pip de manera global

    pip install virtualenv


### 2. Crear un entorno virtual con virtualenv

    virtualenv .venv


### 3. Activar el entorno virtual

Linux:

    source .venv/bin/activate

Windows:
    
        .venv\Scripts\activate


#### 4. Instalar las dependencias del proyecto

    pip install -r requirements.txt


### 5. Ejecutar las migraciones
    
    python manage.py makemigrations
    python manage.py migrate


### 6. Crear un super usuario

    python manage.py createsuperuser
    User:
    Email:
    Password:


### 7. Ejecutar el servidor
    python manage.py runserver [host:port]

