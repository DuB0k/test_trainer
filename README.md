# TestTrainer website

This project helps user learning through the process of solving different test examns.
The site allow user to create custom test and displays some useful statistics about the test learning experience.

Home page [https://test-trainer-dub0k.c9.io/](https://test-trainer-dub0k.c9.io/)
Admin page[https://test-trainer-dub0k.c9.io/admin](https://test-trainer-dub0k.c9.io/admin) 

## Requirements

This project use django1.8 and Python3.4
See requirements.txt for more info

## Starting django app

#####1) Create virtual env
```python
     $ virtualenv -p /usr/bin/python3.4  env
     $ source env/bin/activate
     $ pip install django
     $ which django-admin
```
#####2) Start django project
```python
     $ django-admin.py startproject testTrainer
     $ python manage.py migrate
     $ python manage.py createsuperuser
     $ python manage.py runserver  $IP:$PORT
```
#####3) Create repo
```python
     $ git init
     $ git add .
     $ git remote add origin https://github.com/DuB0k/test_trainer.git
     $ git commit -m "First commit"
     $ git push -u origin master
```

## Django steps
#####1) Create the project:
```python
	$ django-admin startproject testTrainer
```
#####2) Change dir to the django root directory:
```python
     $ cd testTrainer
```
#####3) Create tables in the database:
```python
     $ python manage.py migrate
```
     Note:
     The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app
#####4) Create app tests:
```python
     $ python manage.py startapp tests
```
#####5) Create tests/models.py with some database content
#####6) Install tests app editing INSTALLED_APPS in settings.py
#####7) Create database migrations for tests app model
```python
     $ python manage.py makemigrations tests
```
#####8) Display database sentences of the new migration file created above
```python    
     $ python manage.py sqlmigrate tests 0001
```
#####9) Migrate database
```python 
     $ python manage.py migrate
```
#####10) Create admin user
```python 
     $ python manage.py createsuperuser
```
#####11) Make the tests app modifiable in the admin
Edit tests/admin.py
```python 
     admin.site.register(Test)
```
