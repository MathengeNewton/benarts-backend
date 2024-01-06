## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ # Get the code
$ git clone https://**git url**
$ cd /path/to/directory/backend
```

<br />

> **Step 2** - Edit `.env` and set `DEBUG=True`. This will activate the `SQLite` persistance. 

```txt
DEBUG=True
```

<br />

> **Step 3** - Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://**git url**
$ cd /path/to/directory/backend
```
<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Flask Environment

```bash
$ # CMD 
$ set FLASK_APP=run.py
$ set FLASK_ENV=development
$
$ # Powershell
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

<br />

> Start the app

```bash
$ flask run
```

At this point, the app runs at `http://127.0.0.1:5000/`. 

<br />

## ✨ Code-base structure

The project has a simple, intuitive structure presented bellow:

```bash
< PROJECT ROOT >
   |-- instance
        |-- nation.db
   |-- media/
        |-- < media files >
   |-- nginx
        |-- appseed-app.conf
   |-- app/
        |-- api/
            |-- < Api files >  
        |-- models/
            |-- < Model Files files >  
        |-- views/
        |         |-- < Api files >  
        |-- static/
        |    |    |-- <css, JS, images>
        |    |
        |-- templates/
        |         |-- < Jinja template page files >
        |-- __init__.py
        |-- config.py
        |-- extensions.py
        |-- utils.py
   |
   |-- requirements.txt
   |
   |-- CHANGELOG.md
   |
   |-- Dockerfile
   |
   |-- docker-compose.yaml
   |
   |-- gunicorn-cfg.py
   |
   |-- LICENCE.md
   |
   |-- log.json
   |
   |-- Procfile
   |
   |-- README.md
   |
   |-- run.py
   |  
   |-- runtime.txt
   |
   |-- ************************************************************************
```