from django_filters import FilterSet
from .models import Movie


class MovieFilterSet(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'actor': ['exact'],
            'director': ['exact'],
            'country': ['exact'],
            'status_cinema': ['exact'],
            'year': ['gt', 'lt'],
            'janre': ['exact']
        }