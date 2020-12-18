# Football Players CRUD Django #

A football player CRUD system made with Django.

### How do I get set up? ###

- Pull the project to your local machine and open the terminal in the project root folder.
- Create a secret key with the following command.

python -c "import secrets; print(secrets.token_urlsafe())"
    
- Create a .env file in project root folder with the contents below. This .env file have secret credentials we don't need to share in Github.

DEBUG=True<br/>
SECRET_KEY=YOUR GENERATED KEY<br/>
DATABASE_USER=YOUR POSTGRES DATABASE USER<br/>
DATABASE_PASSWORD=YOUR POSTGRES DATABASE PASSWORD<br/>
DATABASE_HOST=YOUR POSTGRES DATABASE HOST<br/>
DATABASE_PORT=YOUR POSTGRES DATABASE PORT<br/>

- Criate a virtual environment folder in the project root folder and activate the environment.

python -m venv venv</br>
    
venv\Scripts\activate
    
- Intall project python dependencies from requirements.txt

pip install -r requirements.txt
    
- Excute project migrations

python manage.py migrate

- Run the project

python manage.py runserver

### Who do I talk to? ###

* Repo owner: Daniel Lima
* Email: daniellima2297@gmail.com
