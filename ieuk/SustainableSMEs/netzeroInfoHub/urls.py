from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home page"),
    path("details/<int:id>", views.detailed, name="Home page"),
]