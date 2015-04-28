# TestTrainer website

This project helps user learning through the process of solving different test examns.
The site allow user to create custom test and displays some useful statistics about the test learning experience.

Home page [https://test-trainer-dub0k.c9.io/](https://test-trainer-dub0k.c9.io/)
Admin page[https://test-trainer-dub0k.c9.io/admin](https://test-trainer-dub0k.c9.io/admin) 

## Requirements

This project use django1.8 and Python3.4 

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
