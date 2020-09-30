from django.urls import path
from todo.views import index, updateTask, deleteTask

urlpatterns = [
    path('', index, name="list"),
    path('update/<str:pk>/', updateTask, name="update"),
    path('delete/<str:pk>/', deleteTask, name="delete")

]