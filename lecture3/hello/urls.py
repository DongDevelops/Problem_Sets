from django.urls import path

from . import views

urlpatterns = [
    path("", ivews.index, name="index")
]