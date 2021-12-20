# BlogX

A blog using HTMX and Django

## Get it up and running

### **Install poetry and create virtual environments**

```bash
pip install -U pip poetry
poetry install && poetry shell
```

### **Running project**

```bash
./manage.py migrate
./manage.py loaddata dev_data.json
./manage.py runserver
```

## Running project with Docker

1. docker compose up -d --build
2. docker compose exec web python manage.py migrate
3. docker compose exec web python manage.py loaddata dev_data.json

*Open in your browser, visit <http://127.0.0.1:8000> and login to /admin with admin/123456a@*
