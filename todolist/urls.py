from django.contrib import admin
from django.urls import path
import todolist.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('collection/<str:collection_slug>/', views.get_tasks, name="get-tasks"),
    path('delete-collection/<int:pk>/', views.delete_collection, name="delete-collection"),
    path('add-collection/', views.add_collection, name="add-collection"),
    path('add-task/', views.add_task, name="add-task"),
    path('delete-task/<int:pk>/', views.delete_task, name="delete-task")
]
