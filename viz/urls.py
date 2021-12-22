from django.urls import path
from . import views

urlpatterns = [
path('all', views.view_all, name="homepage")]