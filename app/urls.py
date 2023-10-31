from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('<int:stud_id>/deleterecord/', views.deleterecord, name='deleterecord'),
]