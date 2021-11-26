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
**Side Note :**
 * Projects vs. apps
 * An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects. 
**Writing Views :**
 * A view acts as a middle man between our models and templates they are request handlers
 * When creating views then after they should be mapped to urls
 * **Key variables and functions :**
    * HttpResponse ->
	* render() ->
	* include() ->function allows referencing other URLconfs. 
	* path() ->function is passed four arguments, two required: route and view, and two optional: kwargs, and name. 
 * Views can be function based or class based
 
 