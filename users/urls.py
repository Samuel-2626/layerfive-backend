from django.urls import path
from .views import ListUser, DetailUser

urlpatterns = [
  path('<str:pk>/', DetailUser.as_view()),
  path('', ListUser.as_view()),
]