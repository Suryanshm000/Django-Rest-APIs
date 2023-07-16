# Django-Rest-APIs

This is a django application where frontend shows user and admin interfaces and frontend is receiving data from backend Rest APIs.

Rest APIs are built in Django Rest Framework and integrated with token authentication.

This app also includes the Swagger documentation for Rest APIs.

<br>

## Screenshots

Admin and User Views

![Imgur](https://i.imgur.com/r2TN5km.png)

![Imgur](https://i.imgur.com/DLiMNpR.png)

![IMAGE](https://i.imgur.com/bhkiZ51.png)

![Imgur](https://i.imgur.com/0UIc2Iw.png)

![Imgur](https://i.imgur.com/GKaZeyj.png)

![Imgur](https://i.imgur.com/Qdr57yh.png)

<br>

### [Screen recording](https://www.loom.com/share/90d23d3d769f425cb2c0e97737cec845)

<br>

## Rest-API's

There is Token Authentication in Rest-API so first authenticate on API by posting username and password in body then save the token.


[POST] http://127.0.0.1:8000/api/api-token-auth/

<br>
Now do Token Authorization in header as:

Headers = 'Authorization Token a07d0df30589...'


[GET] http://127.0.0.1:8000/api/admin-home

<br>
Post data into the body

[POST] http://127.0.0.1:8000/api/add-app


[GET] http://127.0.0.1:8000/api/app/{id}


[DELETE] http://127.0.0.1:8000/api/app-delete/{id}


[GET] http://127.0.0.1:8000/api/user-home

<br>

Swagger documentation

http://127.0.0.1:8000/swagger

<br>

### Admin credentials

username: testadmin

password: test

### User credentials

username: testuser

password: test

<br>

# Running at localhost

These are the steps to follow in order to run the project on local host: 
<br>

```
git clone https://gitlab.com/suryanshm000/django-rest-api.git`
```

```
cd django-rest-api
```

```
pip install virtualenv
python -m venv <name of environment>
source <name of environment>/bin/activate
pip install -r requirements.txt
```


The *django application* is started via the following command and is accessible on *http://127.0.0.1:8000/*

```
python manage.py runserver
```
<br>

