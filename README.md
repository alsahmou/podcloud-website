# PodCloud Website

This website allows users to upload their podcasts and their respective episodes to generate RSS feeds with XML files, enabling users to listen to their podcasts using podcasts mobile phone application.

<img src="https://i.imgur.com/iTqqm47.png" width="40%">.
<img src="https://i.imgur.com/GCovtE2.png" width="40%">.
<img src="https://i.imgur.com/5QsHiqa.png" width="40%">.



# Setup

 - Install python3.6 by entering the following commands in the terminal:
`$ sudo add-apt-repository ppa:jonathonf/python-3.6`
`$ sudo apt-get update`
`$ sudo apt-get install python3.6`

 - Ensure python3.6 is installed by entering the following command in the terminal:
`$ python3 -V`

 - Install pip3 by entering the following commands in the terminal:
`$ sudo apt-get -y install python3-pip`
`$ sudo apt-get update`

 - Ensure pip3 is installed by entering the following command in the terminal:
`$ pip3 -V`

 - Inside your directory setup a virtual environment by entering the following command in the terminal:
`$ virtualenv -p python3 .`

 - Activate the virtual environment by entering the following command in the terminal:
`$ bin/source activate`

 -Inside your virtual environment install Django by entering the following command in the terminal:
`$ pip3 install django`

 - Inside your virtual environment create a Super User by entering the following command in the terminal: The Super User enables you to access your database using the admin application.
`$ python3 manage.py createsuperuser `

 - Install postgreSQL by entering the following commands in the terminal:
`$ sudo apt-get update`
`$ sudo apt-get install postgresql postgresql-contrib`

 - Switch to postgres account by entering the following command in the terminal:
 `$ sudo -i -u postgres`

 - Switch to a postgres prompt by entering the following command in the terminal:
 `$ psql`

 - You will be logged in and able to interact with the databse management right away

 - Create a new role by entering the following command inside the postgres prompt, replace myuser and mypass with your own username and password:
 `postgres=# create user myuser with encrypted password 'mypass';`

 - Inside the postgres prompt create a database by entering the following command, replace mydb with your database's name:
 `CREATE DATABASE mydb`

 - Grant all database privileges on your database to your user by entering the following command inside the postgres prompt, replace mydb and myuser with your own database name and your username:
 `GRANT ALL PRIVILEGES ON DATABASE mydb to myuser`

 - Store 'SECRET_KEY' from settings.py file in a secure place then, delete 'DATABASES' and 'SECRET_KEY' from settings.py file to the following to use your postgreSQL database and secret key. Put them in a json.config file and replace SECRET_KEY, NAME, USER and PASSWORD with your own values.
 
```
{
    "SECRET_KEY": "'#####'",

    "DATABASES" : {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "#####", 
            "USER": "#####",
            "PASSWORD": "#####",
            "HOST": "127.0.0.1",
            "PORT": "5432"
        }
    }
}
```

 - To finalize the database setup, open the terminal and start the virtual environment then enter the following command.
 `$ python3 manage.py migrate`

 - Find your server's ip address by entering the following command in the terminal:
 `$ curl ifconfig.me`


# Run Website
- To start the website start your virtual environment then enter the following command, replace ip and port with your own ip address:
 `$ python3 manage.py runserver ip:8000`


 



 






