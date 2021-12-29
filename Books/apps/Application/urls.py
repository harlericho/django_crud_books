from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'), 
    path("delete/<id>", views.delete, name="delete"),
    path("edit/<id>", views.edit, name="edit")
]
