## Requirements for Assignment-2
[Read the instruction](https://github.com/STIW3054-A211/e-sulam/blob/main/Assignment-2.md)

## Your Info:
| Photo                          |Matric Number  | Name                | Phone Number     |
| ------------------------------ | ------------- | --------------------|----------------- |
| ![272033](/images/272033.png)  | 272033        | Lee Xiu Niang       | 012-5223989      |

## Introduction
In this assignment, a Telegram Bot that linked to the database of the Web Application for Pusat Kawalan Operasi Bencana (PKOB) which developed in assignment 1 is created using Python programming language. This Telegram Bot is an autoresponder which will automatically reply when the user chat in the telegram bot. There will be command menu which can lead the users how the Telegram Bot functions. A start command which greets the users and remind the users to refer the menu to proceed. A check command to instructs the users how to check the information (IC number, Phone number, Name, Age) of a registered user. The user can check the information of registered by using the registered IC number and phone number. If the IC number and phone number input is invalid, the system will reply with an error message and prompt the users to re-enter them. Lastly, a visit command which give the URL link of the linked PKOB website mentioned. Whenever the user entered an invalid command or in wrong format, the system will reply with an error message too.
## Deployment Guide
1. Deploy the database of website (app: pkob272033) in Heroku Postgres:  
- Get the database credentials settings from Heroku, then Update PKOB/settings.py  
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd79iesnsq1f0vq',
        'USER': 'dryhxgxgtcqhdu',
        'PASSWORD': '72c26e4a03537ef48174c896abf1c7a594947199398ea5e7bc0f27b166fcd655',

        'HOST': 'ec2-34-204-58-13.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
````
- Install psycopg2-binary and Migrate the database to Heroku Postgres
````
$ pip install psycopg2-binary
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
````
- Update requirements.txt
````
$ pip3 freeze > requirements.txt
````
- Update PKOB/setting.py
````
ALLOWED_HOSTS = ['127.0.0.1','pkob272033.herokuapp.com']
````
- Login and Create git remote, then Push to Heroku
````
$ heroku login
$ heroku git:remote -a pkob272033
$ git remote
$ git add .
$ git commit -m "update setting.py"
$ git push heroku master
````  
2. Deploy new app (pkob-272033-bot) for telegram bot at Heroku:
- Get the database credentials settings (app: pkob272033), URL, from Heroku, and Connect inside reply function for hecking information in database
````
conn = psycopg2.connect("postgres://dryhxgxgtcqhdu:72c26e4a03537ef48174c896abf1c7a594947199398ea5e7bc0f27b166fcd655@ec2-34-204-58-13.compute-1.amazonaws.com:5432/d79iesnsq1f0vq")
````
- Get the database credentials settings (app: pkob-272033-bot) from Heroku, then Update PKOB/settings.py
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6va6ijuf5ao9b',
        'USER': 'mqnyjhunlrdusm',
        'PASSWORD': '69c4a8532925231b3e7bdaa68aae27a8d34c65a6d70eb2200e134b6030fbff71',

        'HOST': 'ec2-52-4-197-13.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
````
- Install psycopg2
````
$ pip install psycopg2-binary
````
- Install gunicorn
````
$ pip3 install gunicorn
````
- Create Procfile
````
web: gunicorn PKOB.wsgi
worker: python pkob_telegrambot.py
````
- Update requirements.txt
````
$ pip3 freeze > requirements.txt
````
- Update PKOB/setting.py
````
ALLOWED_HOSTS = ['127.0.0.1','pkob-272033-bot.herokuapp.com']
````
- Login and Create git remote, then Push to Heroku
````
$ heroku login
$ heroku git:remote -a pkob-272033-bot
$ git remote
$ git add .
$ git commit -m "update setting.py"
$ git push heroku main
````  
- Run if the static folder is not configured
````
$ heroku config:set DISABLE_COLLECTSTATIC=1
````
- Turn OFF Dynos: web and ON Dynos: worker (app: pkob-272033-bot) in the Resources section of the app in Heroku

## Result/Output (Screenshot of the output)
MOBILE VERSION:  
![TeleBot_New](/images/TeleBot_New.jpg)

Menu (Commands)  
![TeleBot_Menu](/images/TeleBot_Menu.jpg)

Sample Output  
![Telebot_Sample](/images/Telebot_Sample.jpg)

DESKTOP VERSION:  
Menu (Commands)  
![TeleBotWEB_Menu](/images/TeleBotWEB_Menu.png)

Sample Output
![TeleBotWEB_Sample1](/images/TeleBotWEB_Sample1.png)
![TeleBotWEB_Sample2](/images/TeleBotWEB_Sample2.png)

## Youtube Presentation
https://youtu.be/fvLMP6H1PCM

## List of Python packages (including the version) used for this system
appdirs==1.4.4  
APScheduler==3.6.3  
asgiref==3.4.1  
backports.zoneinfo==0.2.1  
beautifulsoup4==4.9.1  
bs4==0.0.1  
cachetools==4.2.2  
certifi==2020.6.20 
chardet==3.0.4  
cheroot==8.4.5  
distlib==0.3.1  
Django==3.2.8  
filelock==3.0.12  
gunicorn==20.1.0  
idna==2.10  
jaraco.functools==3.0.1  
more-itertools==8.5.0  
Pillow==7.2.0  
psycopg2-binary==2.9.2  
pymongo==3.11.0  
python-dateutil==2.8.2  
python-telegram-bot==13.9  
pytz==2021.3  
pytz-deprecation-shim==0.1.0.post0  
requests==2.24.0  
reverse==0.1.0  
simplejson==3.17.2  
six==1.16.0  
soupsieve==2.0.1  
sqlparse==0.4.2  
tornado==6.1  
tzdata==2021.5  
tzlocal==4.1  
urllib3==1.25.10  
virtualenv==20.0.31  
web.py==0.61  

## References (Not less than 10)
Adylzhan Khashtamov. (2021, January 4). How to Work with PostgreSQL in Python. Khashtamov.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://khashtamov.com/en/postgresql-with-python-and-psycopg2/  

Ali Abdel Aal. (n.d.). Building Your First Telegram Bot: A Step by Step Guide. Toptal.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.toptal.com/python/telegram-bot-tutorial-python

Bots: An introduction for developers. (n.d.). Telegram.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://core.telegram.org/bots

Code Palace. (2021, January 25). Creating a Telegram Bot in Python 3.9 Tutorial (Fast & Easy) [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=PTAkiukJK7E

Code Palace. (2021, August 17). How to create a Telegram Bot for FREE in Python - Commands & Messaging [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=50npIbrXmnI

COLORFUL. (2020, November 15). Create a Telegram Bot and Deploy it to Heroku for Free [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=-yWuLRJhoNI

Dennis Ivy. (2020, January 28). Heroku Postgres Connection | Django (3.0) Crash Course Tutorials (pt 24) [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=TFFtDLZnbSs&ab_channel=DennisIvy

I know python. (2021, January 7). How to create a Telegram Bot using python [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=7qJFtGi0hNQ

pentexnyx. (2021, July 10). Telegram Bot Tutorial Python Heroku [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=fQo_327-AZA

Tech Mind. (2020, November 15). Hosting Python Telegram Bot on Heroku for FREE. [Video]. YouTube.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://www.youtube.com/watch?v=O0MAWtbg34g