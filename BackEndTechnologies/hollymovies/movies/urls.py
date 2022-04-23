from django.urls import path
from movies.views import HomepageView, MoviesListView, jinja2_testing_view, ActorListView, MovieDetailView, ActorDetailView, DirectorListView
from movies.views import DirectorDetailView, ContactView, CreateMovieView, CreateActorView, UpdateMovieView
from movies.views import DeleteMovieView, DeleteActorView, UpdateActorView, CreateDirectorView, UpdateDirectorView, DeleteDirectorView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('actors/', ActorListView.as_view(), name='all_actors'),
    path('actor/<int:pk>', ActorDetailView.as_view(), name='actor_detail'),
    path('movies/', MoviesListView.as_view(), name='all_movies'),
    path('movie/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('directors/', DirectorListView.as_view(), name='all_directors'),
    path('director/<int:pk>', DirectorDetailView.as_view(), name='director_detail'),
    path('testing/', jinja2_testing_view, name='jinja2_testing_view'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('movie/create/', CreateMovieView.as_view(), name='create_movie'),
    path('actor/create/', CreateActorView.as_view(), name='create_actor'),
    path('director/create/', CreateDirectorView.as_view(), name='create_director'),
    path('movie/update/<int:pk>', UpdateMovieView.as_view(), name='update_movie'),
    path('actor/update/<int:pk>', UpdateActorView.as_view(), name='update_actor'),
    path('director/update/<int:pk>', UpdateDirectorView.as_view(), name='update_director'),
    path('movie/delete/<int:pk>', DeleteMovieView.as_view(), name='delete_movie'),
    path('actor/delete/<int:pk>', DeleteActorView.as_view(), name='delete_actor'),
    path('director/delete/<int:pk>', DeleteDirectorView.as_view(), name='delete_director'),

]