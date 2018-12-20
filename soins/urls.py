# Urls de l'application Soins du site VanEsthetique
from django.urls import path
from . import views
app_name = 'soins'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
