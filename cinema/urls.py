from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.getAll, name="all"),
    path("create", views.create, name="create"),
    path("get/<int:id>", views.read, name="read"),
]