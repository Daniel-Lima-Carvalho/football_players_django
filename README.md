# Football Players CRUD Django #

### What is this repository for? ###

* A football player CRUD system made with Django.

### How do I get set up? ###

* Pull the project to your local machine
* Create a secret key
* Create a .env file in project root folder with the contents below. This .env file have secret credentials we don't need to share in Github.

    DEBUG=False
    SECRET_KEY=YOUR GENERATE KEY
    DATABASE_USER=YOUR POSTGRES DATABASE USER
    DATABASE_PASSWORD=YOUR POSTGRES DATABASE PASSWORD
    DATABASE_HOST=YOUR POSTGRES DATABASE HOST
    DATABASE_PORT=YOUR POSTGRES DATABASE PORT

* Criate a virtual env to the project.
* Excute the migrations

    1 - python manage.py migrate

* Run the project

    1 - python manage.py runserver

### Who do I talk to? ###

* Repo owner: Daniel Lima
* Email: daniellima2297@gmail.com