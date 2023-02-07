# ORM
Some Object–relational Mapping(ORM) instructions 


## Using Multiple Database [ Postgres - MySql - Sqlite]
```yaml
DATABASES = {
    'default': {},
    'first': { ## Postgres SQL
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'first_db',
        'USER': 'postgres',
        'PASSWORD': '*******',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'second_db': { # sqlLite DataBase
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'second.db.sqlite3',
    },
    'third_with_mysql':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'third_multiple_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

DATABASE_ROUTERS = ['Routers.routers.AuthRouter', 'Routers.routers.Second_db', 'Routers.routers.Third_db']
```
