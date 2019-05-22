# crayond_backend

# Flask example

Using Flask to build a Restful API Server with Swagger document.

Integration with Flask-SQLalchemy Flask-OAuth extensions.

### Extension:

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)


## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──────crayond_backend/
| |────models/
| | |────__init__.py
| | |────upload/
| |────modules/
| | |────__init__.py
| | |────newsfeed/
| |────util/
|──────app.py
|──────init.py
|──────status.py
|──────loadconfig.py
|──────manage.py
|──────config.yml
|──────requirements.txt


```


## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
### Configuring From Files

#### Example Usage

```
app = Flask(__name__ )
app.config.from_pyfile('config.Development.cfg')
```

#### cfg example

```

##Flask settings
DEBUG = True  # True/False
TESTING = False

##SWAGGER settings
SWAGGER_DOC_URL = '/api'

....


```
## Creating Python virtual environment 
```
$ pip3 install virtualenv
$ python3 -m venv envName
```

## Creating Python virtual environment 
```
$ source envName/bin/activate

```

## Python Migration
### Creating Python Migrtion 
```
$ python manage.py db init

$ python manage.py db migrate

$ python manage.py db upgrade
```
 
## Run Flask
### Run flask for develop
```
$ python app.py
```
In flask, Default port is `5000`

Swagger document page:  `http://localhost:5000/apidocs/#`

