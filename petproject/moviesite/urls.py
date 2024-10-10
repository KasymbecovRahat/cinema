from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='movie_detail'),

    path('profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile_list'),
    path('profiles/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='profile_detail'),

    path('genres/', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='janre_list'),
    path('genres/<int:pk>/', JanreViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='janre_detail'),

    path('countries/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('countries/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='country_detail'),

    path('director/', DirectorListViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('directors/<int:pk>/', DirectorDetailViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='director_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='moments_detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actors/<int:pk>/', ActorDetailViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='actor_detail'),

    path('movie_languages/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_languages_list'),
    path('movie_languages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='movie_languages_detail'),

    path('favorite_movies/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='f_movie_list'),
    path('favorite_movies/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='f_movie_detail'),

    path('favorites/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_list'),
    path('favorites/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='favorite_detail'),

    path('histories/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
    path('histories/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='history_detail'),

    path('ratings/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='rating_detail'),
]


