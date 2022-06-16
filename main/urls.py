from django.urls import path
from . import views
urlpatterns = [
    path('greet/', views.greet, name='greet'),
]