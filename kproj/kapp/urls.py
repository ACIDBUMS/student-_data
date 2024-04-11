from django.urls import path
from . import views

urlpatterns = [
    path("",views.mala,name="mala1"),
    path("add",views.add,name="mark"),
]
