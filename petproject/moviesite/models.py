from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from multiselectfield import MultiSelectField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    date_register = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)

    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True, blank=True, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=50)
    director_age = models.PositiveSmallIntegerField()
    director_bio = models.TextField()
    director_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f'{self.director_name} {self.director_age} {self.director_image}'


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    actor_age = models.PositiveSmallIntegerField()
    actor_bio = models.TextField()
    actor_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return f'{self.actor_name} {self.actor_age} {self.actor_image}'


class Janre(models.Model):
    janre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    year = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country, related_name='movies', on_delete=models.CASCADE)
    director = models.ManyToManyField(Director, related_name='movies')
    actor = models.ManyToManyField(Actor, related_name='movies')
    janre = models.ManyToManyField(Janre, related_name='movies')
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='video', verbose_name='трейлер', null=True, blank=True)
    movie_image = models.ImageField(upload_to='image')
    STATUS_MOVIE = (
        ('pro', 'Pro'),
        ('simple', 'Simple')
    )
    status_cinema = models.CharField(max_length=100, choices=STATUS_MOVIE, null=True, blank=True, default='simple')
    RESOLUTION_CHOICES = [
        (144, '144p'),
        (360, '360p'),
        (480, '480p'),
        (720, '720p'),
        (1080, '1080p'),
    ]
    types = MultiSelectField(choices=RESOLUTION_CHOICES, null=True, blank=True, default=144)

    def __str__(self):
        return self.movie_name

    def get_average_ratings(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return None


class MovieLanguages(models.Model):
    language = models.CharField(max_length=50)
    video = models.FileField(upload_to='video/')
    movie = models.ForeignKey(Movie, related_name='movie_languages', on_delete=models.CASCADE)


class Moments(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_momemts', on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='movie_image/')


class Rating(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i,  str(i)) for i in range(1, 11)], verbose_name='Рейтинг')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replice', null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} {self.movie} {self.stars}'


class Favorite(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)



