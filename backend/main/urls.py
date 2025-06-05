from .views import *
from django.urls import path

urlpatterns = [
    path('api/tasks/', TaskList.as_view()),
    path('api/tasks/<int:id>', TaskDetail.as_view()),
]