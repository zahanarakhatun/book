from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('addbook/', views.addBook, name='addBook'), # views.addBook লিখুন এবং URL Path 'addbook/' ছোট হাতের রাখুন
]