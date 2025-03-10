from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
]