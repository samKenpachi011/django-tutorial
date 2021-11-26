# Django-tutorial
** Understanding django**

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
	* asgi.py --> Asynchronous Server Gateway Interface. It extends the capabilities of WSGI (Web Server Gateway Interface), which is a standard way of communication between the web server and the web applications in most of the python web frameworks like Django.
	* wsgi.py --> needed when deploying a project over wsgi.
	* urls.py --> used t map out incoming requests to views.
	* settings.py -->where all the project configuration reside.
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
 
## Creating Models
**What are models and how do they fit into django:**
 * Models provide a single source of truth for our data. Allow us to define schemas  
 * Each model has a number of class variables, each of which represents a database field in the model.
**Side Note :**
 * Knowing about the ORM-Object Relational Mapper
 * ORM is a powerful technique in django even though it has its pitfalls. It gives us a level of abstraction which makes it easy to work with object.
 * ORM ->Let's us query and manipulate data from a database using an object oriented paradigm thus the developer does not have to write any SQL.
 * Link [ORM-Brief] (https://data-flair.training/blogs/django-orm-tutorial/ https://data-flair.training/blogs/django-orm-tutorial/)
**Getting Back to Models 😃 :**
 * Each model is a python class that subclasses from django.db.models.Model 
 * The Model class has helper functions (Fields,Autofields)
 * Once you have defined your models, you need to tell Django you’re going to use those models. Do this by editing your settings file and changing the INSTALLED_APPS setting to add the name of the module that contains your models.py.
 * Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. 
 * save()->
**Side Note :**
 * Migrations ->Letting django know about changes in the model
 * Migrate  ->Applying migrations to the database
 * Using the interactive shell to interact with the database API
 * using double underscore functions __str__()
 
 
## Djangon Admin 
