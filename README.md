# Football Players CRUD Django #

A football player CRUD system made with Django, Bootstrap in frontend and PostgreSQL database.

### How do I get set up? ###

1 - Pull the project to your local machine and open the terminal in the project root folder.
2 - Create a secret key with the following command.

        python -c "import secrets; print(secrets.token_urlsafe())"
    
3 - Create a .env file in project root folder with the contents below. This .env file have secret credentials we don't need to share in Github.

        DEBUG=True
        SECRET_KEY=YOUR GENERATED KEY
        DATABASE_USER=YOUR POSTGRES DATABASE USER
        DATABASE_PASSWORD=YOUR POSTGRES DATABASE PASSWORD
        DATABASE_HOST=YOUR POSTGRES DATABASE HOST
        DATABASE_PORT=YOUR POSTGRES DATABASE PORT

4 - Criate a virtual environment folder in the project root folder and activate the environment.

        python -m venv venv
    
        venv\Scripts\activate
    
5 - Intall project python dependencies from requirements.txt

        pip install -r requirements.txt
    
6 - Excute project migrations

        python manage.py migrate

7 - Run the project

        python manage.py runserver

### Who do I talk to? ###

* Repo owner: Daniel Lima
* Email: daniellima2297@gmail.com
