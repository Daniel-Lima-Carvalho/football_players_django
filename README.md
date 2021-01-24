# Football Players CRUD Django #

A football player CRUD system made with Django, Bootstrap in frontend and PostgreSQL database.

### How do I get set up? ###

1 - Pull the project to your local machine and open the terminal in the project root folder.</br>

2 - Create a secret key with the following command.
        
Linux
        
        python3 -c "import secrets; print(secrets.token_urlsafe())"

Windows
        
        python -c "import secrets; print(secrets.token_urlsafe())"
        
3 - Create a .env file in the project root with your credentials.

        DEBUG=True
        SECRET_KEY=YOUR GENERATED KEY
        DATABASE_NAME=YOUR POSTGRES DATABASE NAME
        DATABASE_USER=YOUR POSTGRES DATABASE USER
        DATABASE_PASSWORD=YOUR POSTGRES DATABASE PASSWORD
        DATABASE_HOST=YOUR POSTGRES DATABASE HOST
        DATABASE_PORT=YOUR POSTGRES DATABASE PORT

4 - Create a virtual environment in the project root and activate it.

Linux
        
        apt-get install python3-venv
        
        python3 -m venv venv
        
        source venv/bin/activate

Windows

        python -m venv venv
    
        venv\Scripts\activate
    
5 - Intall python dependencies from requirements.txt.

Linux
        
        pip3 install -r requirements.txt

Windows

        pip install -r requirements.txt
    
6 - Excute migrations.

Linux

        python3 manage.py migrate

Windows 
        
        python manage.py migrate

7 - Create a superuser.

Linux

        python3 manage.py createsuperuser

Windows       

        python manage.py createsuperuser
        
8 - Run the project.

Linux
        
        python3 manage.py runserver 0.0.0.0:8000
  
Windows
     
        python manage.py runserver 0.0.0.0:8000
        
### How to set up with Docker? ###

1 - Repeat steps 1 and 2 from the previous setup guide.</br>

2 - Create a .env file in the project root with your credentials.
        
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
        
 4 - Create a superuser
 
        docker exec -it football_players_server bash
        
        python manage.py createsuperuser

### Project Images ###

![Players List Page](https://raw.githubusercontent.com/Daniel-Lima-Carvalho/football_players_django/develop/static/players/images/project/project-1.png)

![Create Player Page](https://raw.githubusercontent.com/Daniel-Lima-Carvalho/football_players_django/develop/static/players/images/project/project-2.png)

### Who do I talk to? ###

* Repo owner: Daniel Lima
* Email: daniellima2297@gmail.com
