# mini_wallet_exercise

CLONE the project by using Git clone "git link"

you have to setup virtual environment to install all the respective packages by Python -m venv virtualenvironment
 
to install all the required packages you need to download requirements.txt file and run command pip install -r requirements.txt in the terminal.
  
use comman python manage.py makemigrations in order to make migrations.
  
use command python manage.py migrate to migrate the missing databases or models.
  
to start the celery workers we have to open new terminal and activate virtual environment then use command celery -A miniwallet worker -l INFO.

to RUN the server use command Python manage.py runserver.
