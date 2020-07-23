
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main_page,name="main_page"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('<int:id>',views.view_item,name="view"),
]
