from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList, name='postlist'),
    path('writepost/', views.writePost, name='writepost'),
    path('postescrito/<int:id>', views.readPost, name='readpost'),
]