from django.urls import path
from . import views


urlpatterns = [
    path("add_book_scan", views.add_book_scan, name="add_book_scan"),
    path("add_book", views.add_book, name="add_book"),
    path("", views.index, name="index"),
]
