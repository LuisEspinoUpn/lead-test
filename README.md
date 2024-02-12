# leadmaster

# Sin Docker - Nuevo Proyecto
- python -m virtualenv lead_venv (solo una vez)
- source lead_venv/Scripts/activate
- pip install poetry
- pip install django
- django-admin startproject app
- Crear archivo `pyproject.toml` en la raiz
- poetry install
- python manage.py startapp api
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

# Sin Docker - Levantar Proyecto - Windows
- `pip install virtualenv`
- `python -m virtualenv lead_venv` (solo una vez)
- `source lead_venv/Scripts/activate`
- `lead_venv\Scripts\activate` (solo si no funciona la linea anterior)
- `pip install poetry` (instala la  libreria poetry)
- `poetry install` (solo una vez o cuando adicionas librerias en pyproject.toml)
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser` 
- `python manage.py runserver`
  