from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from node import views
from django.views.decorators.csrf import csrf_exempt
from node import views

urlpatterns = [
    path("",views.index,name='index'),
    path("datasets/",views.datasets,name='datasets'),
    path("developers/",views.developers,name='developers'),
    path("query/<str:uuid>/",views.query,name='query'),
    path("dataset/add/",views.add_datasets,name='add_datasets'),
    path("delete/dataset/<str:uuid>/",views.add_delete,name='add_datasets'),
    path("login/",views.login_v,name='login_v'),

]