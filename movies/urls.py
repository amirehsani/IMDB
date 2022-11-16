from django.urls import path
from .views import movies_list, movie_detail, movie_add, movie_edit, movie_delete
# views should be defined, then we won't have a problem with the import above

urlpatterns = [
    # 3 elements in each path; 1. the path, 2. the view name, 3. URL name
    path('movies/', movies_list, name='movies_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/<int:pk>/edit', movie_edit, name='movie_edit'),
    path('movies/<int:pk>/delete', movie_edit, name='movie_delete'),
    path('movies/add/', movie_add, name='movie_add')
]
