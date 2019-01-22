# Création d'un nouveau projet DJANGO
## Installer un environnement virtuel avec [PIPENV](https://pipenv.readthedocs.io/en/latest/)
```console
pip install pipenv
```
## Création du projet Van Esthetique
```console
django-admin startproject VanEsthetique
```
## Installer DJANGO dans l'environnement Virtuel
```console
cd VanEsthetique 
pipenv --python 3.6
pipenv install Django
```

## Création de la base de donnée PostgreSQL
```sql
CREATE DATABASE "BD_Soins"
    WITH 
    OWNER = "Angel"
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "Soins"
    IS 'Base de données Soins pour site Multi-langue
```
## Modifier le fichier setting.py du projet afin de pointer vers la base créée
```python
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # on utilise l'adaptateur postgresql
        'NAME': 'BD_Soins', # le nom de notre base de donnees creee precedemment
        'USER': 'Angel', # attention : remplacez par votre nom d'utilisateur
        'PASSWORD': 'angel',
        'HOST': '',
        'PORT': '5432',
    }
}
```
## Installer le module Python [psycopg2](https://pypi.org/project/psycopg2/) permettant de se connecter à PostgreSQL
```console
pipenv install psycopg2-binary
```
## lancer la migration de la base de donnée
```sh
./manage.py migrate
```
Permet de créer les tables PostgreSQL de l'administration Django 
## lancer le serveur DJANGO en local 
```bash
pipenv shell (lancer une seule fois )
./manage.py runserver
```
## création d'application Django 
```bash
./manage.py startapp soins
```
## Rajouter l'application nouvellement créée dans le fichier setting.py
```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'soins',
]
```
## Créer le modèle de donnée Soins à l'aide du fichier models.py de l'application soins
```Python
from django.db import models

class Family_Care(models.Model):
    name = models.CharField('nom', max_length=64, unique=True)
    description = models.TextField('description')
    def __str__(self):
        return self.name

class Care(models.Model):
    name = models.CharField('nom du soin', max_length=64, unique=True)
    family = models.ForeignKey(Family_Care, on_delete=models.CASCADE)
    price = models.DecimalField('Prix' max_digits=5, decimal_places=0)
    def __str__(self):
        return self.name
```
## Créer la vue Index 
```python
from django.views import generic
from .models import Care

class Index(generic.ListView):
    model = Care
    context_object_name = "cares"
    template_name = 'index.html'
    queryset = Care.objects.all().select_related()
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
```

## Créer le dossier static
Copier les fichiers CSS, JS, IMG et FONTS dans des dossier sous le dosier static de l'application

## Créer les templates dans le dossier template
Créer les templates base.html, liste_soins.html et index.html

## Créer le fichier urls.py dans l'application Soins
```Python
from django.urls import path
from . import views
app_name = 'soins'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
```

## Modifier le fichier urls.py du projet
```Python
from django.urls import include, path
from django.contrib import admin
from soins  import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('soins/', include('soins.urls', namespace='soins')),
]
```

## Lancer la génération du fichier Migration (nécessaire à la création de la base de donnée)
```bash
./manage.py makemigrations
./manage.py migrate
```
## mettre à jour le fichier admin.py de l'application pour la partie administration

```Python
from django.contrib import admin
from .models import Care, Family_Care

admin.site.register(Family_Care)
admin.site.register(Care)
```

## Créer le super user pour l'administration du site

```bash
./manage.py createsuperuser
```

## Internationaliser le site

* Extraire les textes à traduire dans le fichier locale/it/LC_MESSAGES/django.po en lançant la commande
  
```bash 
./manage.py makemessages -l it  [messages en Italien]
```

* Modifier le fichier locale/it/LC_MESSAGES/django.po à l'aide d'un éditeur de texte
  *Traduire en italien les balises msgstr*
``` gettext
#: .\VanEsthetique\settings.py:139
msgid "Italian"
msgstr "Italiano"
```

* Compiler le fichier locale/it/LC_MESSAGES/django.po (génération .mo) en lançant la commande
  
```bash 
./manage.py compilemessages -l it  [messages en Italien]
```



## modifier le fichier setting.py 
modifier ce fichier et suivre les instruction sur la[vidéo youtube](https://youtu.be/xI97sLMd1rM)
## Attention 
Faire attention au nom de fichier (il faut respecter la case sur linux alors que Windows est plus permitif)
faire attention à l'outil PIPENV qui peut faire planter le serveur, si plantage ne pas lancer **PIPENV shell** mais uniquement **./manage.py runserver**

## Extraire les données des modèles d'une application
``` bash
./manage.py dumpdata soins > soins/dumps/soins.json
```

## transférer le dépôt GIT sur Heroku (après commit du dépôt local)

``` bash
git push heroku master
```

## Changement des données extraites au format JSON dans modèle application sur serveur HEROKU

``` bash
heroku run python manage.py loaddata soins/dumps/soins.json
```

## instattations de django-jet pour administrer le site

```bash
pipenv install django-jet
``` 

[Suivre les instructions de la documentation de JET]((https://jet.readthedocs.io/en/latest/))

Reproduire sur le serveur de production 
et surtout lancer la commande : 
