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
	* path is passed four arguments, two required: route and view, and two optional: kwargs, and name. 
 * Views can be class based or function based
 * Class Views allow you to structure your views and reuse code by harnessing inheritance and mixins.

**Side Note: Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, class-based views have an as_view() :**
 * Link [ClassBased Views](https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/)  
 * key term (Mixin)->Mixins are a form of multiple inheritance where behaviors and attributes of multiple parent classes can be combined. 
 * Link [GenericViews](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/)
## Creating Models: Part2
**What are models and how do they fit into django:**
 * Models provide a single source of truth for our data. Allow us to define schemas  
 * Each model has a number of class variables, each of which represents a database field in the model.
**Side Note :**
 * Knowing about the ORM-Object Relational Mapper
 * ORM is a powerful technique in django even though it has its pitfalls. It gives us a level of abstraction which makes it easy to work with object.
 * ORM ->Let's us query and manipulate data from a database using an object oriented paradigm thus the developer does not have to write any SQL.
 * Link [ORM-Brief](https://data-flair.training/blogs/django-orm-tutorial/)
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
 * filter,using create,delete()
 * Link [Meta class](https://www.geeksforgeeks.org/meta-class-in-models-django/)
 
## Djangon Admin 
**Note :**
 * Link [DjangoAdmin](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
 * In web development sites need to have an admin side for your staff or clients to add, change, and delete content .
 * Django entirely automates creation of admin interfaces for models include forms which by default take up the html representation of the datafields for which they have been defined.
 * Users are created using the __*createsuperuser*__ command
 * To display models on the admin site we have to register them in the admin.py
 * The register function is used to add models to the Django admin so that data for those models can be created, deleted, updated and queried through the user interface.
 * syntax -> __*admin.site.register(<ModelName>)*__
 
**Side Note :**
 * The ModelAdmin class is the representation of a model in the admin interface 
 * One can register multiple models using the register decoration
 * ** The ModelAdmin is very flexible. It has several options for dealing with customizing the interface :**
    * date_hierarchy 
	* fields
	* exclude
	* empty_value_display
	* fieldsets
	* filter_horizontal
	* filter_vertical
	* form
	* formfield_overrides
	* list_display
	* list_editable
	* list_filter 
	* radio_fields
 * There are also custom template options to override or extend the default admin templates	
 * **InlineModelAdmin objects :**
    * This class allows us to edit a model on the same page as a parent model.
	* InlineModelAdmin shares many of the same features as ModelAdmin, and adds some of its own (the shared features are actually defined in the BaseModelAdmin superclas
	* There are 2 subclasses: TabularInline, StackedInline
 * Overriding admin templates
 * Some changes need for a AdminSite instance to be created.
 * A Django administrative site is represented by an instance of django.contrib.admin.sites.AdminSite; by default, an instance of this class is created as django.contrib.admin.site and you can register your models and ModelAdmin instances with it.
 * **Not every template in contrib/admin/templates/admin may be overridden per app or per model.** 

## More on Views: Part 3	
**Covered :**
 * A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template.
 * To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.->for example: /newsarchive/<year>/<month>/.
 * **Views are responsible for mainly two things :**
    * Returning an HttpResponse
	* Raising an Exception
	
 * **TEMPALTES [templates](https://docs.djangoproject.com/en/3.2/topics/templates/) -> are a way of separating design from python code:There are four constructs  of the Django Template Language:**	
    * tags
	* variables 
	* filters
	* comments
	
## Cutting Down Code: Part 4	
**Covered :**
 * Updating the templates and adding forms
 * CSRF token (Cross Site Request Forgeries)
 * request.POST is a dictionary-like object that lets you access submitted data by key name.
 * Using the HttpResponseRedirect which takes a single argument: the URL to which the user will be redirected
 * Using ListView and DetailView. Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular type of object.”	
 
## Testing : Part 5 
**Covered :**
 * Tests are ways to check the behaviour of our code in terms of returning the expected output
 * Tests help to identify problems in our code and help prevent them
 * Tests can have many strategies for one [TDD in Django](https://medium.com/the-andela-way/test-driven-development-with-django-ccb179171dcd)
 * Django has test tools to help in writting tests [TestingTools](https://docs.djangoproject.com/en/3.1/topics/testing/tools/#django.test.TestCase)
 * **Testing tools :**
    * Setting up the test environment using setup_test_environment() which installs a template renderer which will allow us to examine some additional attributes on responses.
    * Test Client ->simulate a user interacting with the code at the view level(simulate GET/POST requests on a URL and observe the response)
 * **Best Practices :**
    * Have a separate TestClass for each model or view
	* Have a separate test method for each set of conditions you want to test
	* Have test method names that describe their function
	* [Writing and running tests](https://docs.djangoproject.com/en/3.1/topics/testing/overview/)
	* [Advanced Topics](https://docs.djangoproject.com/en/3.1/topics/testing/advanced/)

## Break 😫

## Customizing the app’s look and feel: Part 6
**Covered :**
 * Static files ->Images,Css,JavaScript necessary to render the complete web page.
 * Django.contrib.staticfiles ->it collects static files from each of your applications into a single location that can easily be served in production.
 * Creating a static dir to hold static files
 * Using the load static tag to load static files.