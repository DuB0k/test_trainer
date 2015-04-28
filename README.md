'https://test-trainer-dub0k.c9.io/' and the admin page from 
'https://test-trainer-dub0k.c9.io/admin'.

## Starting django app

1) Create virtual env
     $ virtualenv -p /usr/bin/python3.4  env
     $ source env/bin/activate
     $ pip install django
     $ which django-admin

2) Start django project
     $ django-admin.py startproject testTrainer
     $ python manage.py migrate
     $ python manage.py runserver  $IP:$PORT

3) Create repo
     $ git init
     $ git add .
     $ git remote add origin https://github.com/DuB0k/test_trainer.git
     $ git commit -m "First commit"
     $ git push -u origin master
