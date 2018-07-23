# django_site
common lounge django project

# Creating virtual environment
> mkvirtualenv env
(env)> 
this env folder does not exist in the directory
the env comes already activated
> workon env
(env)> deactivate
> 

> python -m venv env
> env\Scripts\activate
(env)> deactivate
> 

> virtualenv env
> env\Scripts\activate
(env)> deactivate
>

# Create django project
(env)> django-admin startproject mysite
This command creates a folder nysite and puts all the root file and folder that are needed for 
the django project. 

(env)> django-admin startproject mysite .
This command creates the project folders in the same directory

Set the timezone for your country time by setting the value of TIME_ZONE from the timezones for 
example TIME_ZONE = 'Europe/Paris' and don't forget to set `USE_TZ = False` for the timezone to
take effect in the server

# Create django app
(env)> python manage.py startapp blog

To include the app in the project just add the app name in the INSTALLED_APPS = [...] in mysite/
settings.py

# Creating our blog model
We need to make the model for our blog and for that we need all the necessary fields like
title, author, text, publish_date, created_date and a method to publish blogs