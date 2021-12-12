# Recipe REST API

An example REST API for a Recipe app, built with Django, Django REST Framework, and Docker and docker-compose, using Test Driven Design (TDD).

## Status

[![Build Status](https://app.travis-ci.com/erinkelsey/recipe-rest-api-django.svg?branch=main)](https://app.travis-ci.com/erinkelsey/recipe-rest-api-django)

## Build

    $ docker-compose build

## HOW-TO: Run Commands on Container

Start Django project:

    $ docker-compose run app sh -c "django-admin.py startproject app"

Create app in Django project:

    $ docker-compose run app sh -c "python manage.py startapp core"

Run tests in Django project:
$ docker-compose run app sh -c "python manage.py test && flake8"

Make migrations in Django project:

    $ docker-compose run app sh -c "python manage.py makemigrations <app_name, optional>"
