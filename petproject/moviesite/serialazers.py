from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'date_register', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'phone_number', 'date_register', 'status']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name', 'director_image', 'director_bio']


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name', 'director_age', 'director_bio', 'director_image']


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_age', 'actor_bio', 'actor_image']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_image', 'actor_bio']


class JanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = ['janre_name']


class RatingSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()

    class Meta:
        model = Rating
        fields = ['author', 'movie', 'stars', 'parent', 'text', 'created_date']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    janre = JanreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['movie_name',  'year', 'country', 'janre', 'movie_image', 'status_cinema']


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    director = DirectorListSerializer(many=True, read_only=True)
    actor = ActorSerializer(many=True, read_only=True)
    janre = JanreSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    average_ratings = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director',
                  'actor', 'janre', 'movie_time', 'description',
                  'movie_trailer', 'movie_image', 'status_cinema', 'types',
                  'ratings', 'average_ratings']

    def get_average_ratings(self, obj):
        return obj.get_average_ratings()


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video', 'movie']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie', 'movie_moments']


class FavoriteSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = Favorite
        fields = ['user', 'created_date']


class FavoriteMovieSerializer(serializers.ModelSerializer):
    cart = FavoriteSerializer()
    movie = MovieListSerializer()

    class Meta:
        model = FavoriteMovie
        fields = ['cart', 'movie']


class HistorySerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    movie = MovieListSerializer()

    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']
