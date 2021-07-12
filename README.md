# Django-app-tutorial
Django app tutorial which walks through creating a basic poll application

## Set up default python version with oh-my-zshrc

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
