# Django-tutorial
Django app tutorial which walks through creating a basic poll application

## Set up default python version with oh-my-zsh

```
~ vi .zshrc
~ alias python=/usr/local/bin/python3
```

## Install Django

```
~ python -m pip install Django
```

### Check Django version

#### Option 1

```
~ python
>>> import django
>>> print(django.get_version())
>>> 3.2.5
```

#### Option 2

```
~ python -m django --version
> 3.2.5
```
## Create Django project

```
django-admin startproject app
```

## Run Django Development Server

```
~ python manage.py runserver 8000
```

## Create Postgresql Database

```
CREATE DATABASE polls
    WITH
    OWNER = polls
    ENCODING = 'UTF8';
```

## Setup Database ENGINE

In `settings.py` edit this  bloc :

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'polls',
    }
}
```

## Run migration to create the tables

```
➜  django-project git:(main) ✗ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

## Create models

Add this to `polls/models.py`

```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## Add the polls app to the project

In `project/settings.py` edit this bloc:

```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Include the polls app

Run this command :

```
➜  django-project git:(main) ✗ python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

## Check Sqlmigrate command

The sqlmigrate command takes migration names and returns their SQL:

```
➜  django-project git:(main) ✗ python manage.py sqlmigrate polls 0002
BEGIN;
--
-- Alter field choice_text on choice
--
ALTER TABLE "polls_choice" ALTER COLUMN "choice_text" TYPE varchar(250);
--
-- Alter field question_text on question
--
ALTER TABLE "polls_question" ALTER COLUMN "question_text" TYPE varchar(250);
COMMIT;
```

Optionally, perform system check:
```
➜  django-project git:(main) ✗ python manage.py check;
System check identified no issues (0 silenced).
```

## Create model tables

Run migrate again to create model tables in database:

```
➜  django-project git:(main) ✗ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
  Applying polls.0002_auto_20210713_1558... OK
```

## Sum up :
1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.

## Play with python api

See https://docs.djangoproject.com/en/3.2/intro/tutorial02/

```
python manage.py shell
```
## Django Admin

### Create admin User

```
python manage.py createsuperuser
```
## Add first views

Edit `polls/views.py`

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

## Wire first views to urls

Edit `polls/urls.py`

```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

## Unit Test

### Write

Create `tests.py` file in the polls folder:

```
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

### Run

`python manage.py test polls`
