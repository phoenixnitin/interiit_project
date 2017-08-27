# InterIIT Backend
Follow these steps to setup the environment:
1. Clone this repository
2. Install pip, virtualenv and postgresql

  sudo apt-get install python-pip postgresql-contrib postgresql-client-common
  sudo pip install virtualenv
3. create virtualenv 

  example virtualenv virenv
4. activate virtualenv

  source virenv/bin/activate
5. install requirements from requirements.txt file

  cd interiit_project
  pip install -r requirements.txt
6. configure postgresql

  sudo su - postgres
  
  psql
  
  create database interiitdb;
  
  create user interiituser with password 'interiituser1234';
  
  grant all on database interiitdb to interiituser;
  
  \q
  
  exit
7. create migrations for the database and the migrate

  python manage.py makemigrations interiit_app
  
  python manage.py migrate
8. Test your server:

  python manage.py runserver
  
  Open browser and check the address
