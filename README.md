# Django-tutorial
** Understanding django

## What is Django

## Why Django

## Django vs Other frameworks

**Covered :**
 * Make sure Python,Django,Django-admin are installed

## Part 1: Creating a Project
**Covered :**
 * Using the django-admin startproject to create a project ->django-admin createproject mysite
 * Django helps create a project with default files and configurations
 * **Understanding what the default files do :**
	* __init__.py --> for python to treat this folder as a package.
	* asgi.py -->
	* wsgi.py --> needed when deploying a project over wsgi
	* urls.py -->
	* settings.py -->
 * Using the manage.py to do administrative tasks same as django-admin
 * Using manage.py to run the built in django server ->python manage.py runserver
 * Creating an Application (Django comes with a utility that automatically generates the basic directory structure of an app thus saving you time in creating directories)
 * Creating an app ->python manage.py startapp <app-name> eg. python manage.py startapp polls 
 * **Understanding what the default files in an app do :**
	* admin.py --> layout for the admin site/how it is going to look like
	* migrations --> generating database tables
	* apps.py --> configuration for the app
	* models.py --> used to define model classes that communicate with the database
	* tests.py --> writing unit tests
	* views.py --> every data exchange needs to have a request/response thats where views comes in
 
 
 