from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("health/", views.health, name="health"),
    path("hello/", views.hello, name="hello"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("health/", views.health, name="health"),
    path("hello/", views.hello, name="hello"),
    path("add/", views.add, name="add"),
]