# MyPersonalSite

## Table of contents
* [Background](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## Background
This is a project that I created in May 2020. 
It was inspired by two influential individuals whom I have yet to meet. 
One of them is Paul Graham and the other is Patrick Collison.
They have personal sites of their own which I tend to visit quite frequently to gain insight and mold my ways of thinking.

This project yields the result of my web hosted site which can be accessed here: [CoreyJ](https://coreysjordan.com)

	
## Technologies
Project is created with:
* CSS3
* HTML5
* SQLite
* Javascript
* Python 3.7.6
* Django 3.0.5
 
	
## Setup
To run this project, download the files and then run the following commands in your terminal:

Command | Description
-------------|--------------------------------
$ cd ../pages | Navigate to the pages directory which will likely be located in your downloads folder.
$ pipenv install django==3.7.6 |Use this command to create a new virtual environment and install django.
$ pipenv shell | Use this command to activate your virtual environment.
$ python manage.py migrate| Use this command to migrate your files from the database.
$ python manage.py runserver | Use this command to kick-off the server on your local machine.


After running all of the commands above visit http://127.0.0.1:8000/ - the site should be deployed and visible on TCP port 8000 of your local machine.


A great resource for learning step by step Django, SQLite, and project building using this backend framework can be accessed here: [wsvincent](https://github.com/wsvincent/djangoforbeginners)
