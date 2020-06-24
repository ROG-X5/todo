from django.urls import path

from .views import home, addTask, completeTodo, deleteComplete

urlpatterns = [
    path('', home, name='home'),
    path('add', addTask, name='add'),
    path('complete/<task_id>/', completeTodo, name='complete'),
    path('deletecomplete', deleteComplete, name='deletecomplete'),
]