# Football Players CRUD Django #

A football player CRUD system made with Django, Bootstrap in frontend and PostgreSQL database.

### How do I get set up? ###

1 - Pull the project to your local machine and open the terminal in the project root folder.</br>

2 - Create a secret key with the following command.

        python -c "import secrets; print(secrets.token_urlsafe())"
    
3 - Create a .env file in project root folder with the contents below. This .env file have secret credentials we don't need to share in Github.

        DEBUG=True
        SECRET_KEY=YOUR GENERATED KEY
        DATABASE_NAME=YOUR POSTGRES DATABASE NAME
        DATABASE_USER=YOUR POSTGRES DATABASE USER
        DATABASE_PASSWORD=YOUR POSTGRES DATABASE PASSWORD
        DATABASE_HOST=YOUR POSTGRES DATABASE HOST
        DATABASE_PORT=YOUR POSTGRES DATABASE PORT

4 - Create a virtual environment folder in the project root folder and activate the environment.

        python -m venv venv
    
        venv\Scripts\activate
    
5 - Intall project python dependencies from requirements.txt

        pip install -r requirements.txt
    
6 - Excute project migrations

        python manage.py migrate

7 - Run the project

        python manage.py runserver
        
### How to set up with Docker? ###

1 - Repeat steps 1 and 2 from the previous setup guide.</br>

2 - Create a .env file in project root folder with the contents below. This .env file have secret credentials we don't need to share in Github.
        
<pre>
  DEBUG=True
  SECRET_KEY=YOUR GENERATED KEY
  DATABASE_NAME=YOUR POSTGRES DATABASE NAME
  DATABASE_USER=YOUR POSTGRES DATABASE USER
  DATABASE_PASSWORD=YOUR POSTGRES DATABASE PASSWORD
  DATABASE_HOST=<b>postgres_database</b>
  DATABASE_PORT=<b>5432</b>
</pre>
        
 3 - In the project root folder execute the following command.
        
        docker-compose up

### Who do I talk to? ###

* Repo owner: Daniel Lima
* Email: daniellima2297@gmail.com
