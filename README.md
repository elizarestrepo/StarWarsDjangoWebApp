# Star Wars Django Web Application
An Web Application with Django in conjuntion with the SWAPI, to search for star wars movies.

## Requirements:

* Django 3.1.7
* Django RestFramework 3.12.2
* Django-cors-headers 3.7.0
* Requests 2.25.1


## Getting started

First create a virtual enviroment with python as following:

* python3 -m venv "venv-name"

And then activate it with:

* source venv-name/bin/activate

If you do not have the python virtual enviroment in your system, install it with:

* pip install virtualenv

Then install of the requirements written in the "requirements.txt" file with pip as following:

* pip install -r requirements.txt

Finally to run the server, on the console:

* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver


Search suggestions could not be completed, so the following movies exist in the database:

* A New Hope
* The Empire Strikes Back
* Return of the Jedi
* The Phantom Menace
* Attack of the Clones
* Revenge of the Sith