# Async X Sync in Django

Simple project to test performance beetween Async and Sync requests over django views. I have used a Star Wars API from https://swapi.dev/
to make the requests and send to our views.

###### WARNING! This project is only for local testing, it's not prepared for deployment into remote server.

## Prerequisites

* Python 3.8^

## Getting Started

Steps to build and run project:

1. `cd` to root of project
2. `python manage.py makemigrations`
3. `python manage.py migrate`
3. `python manage.py runserver`

## Results

### Sync

<img alt="GitHub last commit" src="https://github.com/johnatasr/Be-The-Hero-Mobile/blob/master/screens/6.png" width="250">

Time : 1.69 seconds

### Async

<img alt="GitHub last commit" src="https://github.com/johnatasr/Be-The-Hero-Mobile/blob/master/screens/6.png" width="250">

Ps. In a synchronized view, I used a class-based view, but in the asynchronous view on a developer server it is not compatible to use, 
so I did it in function based views.

Time : 0.87 seconds

## Conclusion

The request speed in my tests it's was about 50% more faster to async views. In future I want to make async views in Class Based Views 