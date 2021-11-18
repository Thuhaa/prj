from django.urls import path
from . import views

urlpatterns = [
path('all', views.homepage_view, name="homepage")]