from django.contrib import admin
from django.urls import path
from Projects import views

urlpatterns = [
    path('<int:id>',views.home,name='projects_home')
]