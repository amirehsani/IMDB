from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=63)
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    # auto_now_add: the time the instance was created
    # auto_now: the time the instance was modified

    def __str__(self):
        return self.title
    # lets us see the results by movie TITLE


class Role(models.Model):
    title = models.CharField(max_length=63)
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Crew(models.Model):
    MALE = 1
    FEMALE = 2
    GENRE_CHOICE = ((MALE, 'Male'), (FEMALE, 'Female'))
    # a tuple is used here because the dataset should be iterable
    # lists can also be used

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENRE_CHOICE, default=MALE)
    avatar = models.ImageField(upload_to='crew/avatars', null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='movies/avatars', null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    crew = models.ManyToManyField(Crew, through='MovieCrew')
    # Django automatically creates a pivot table for any ManyToMany relation
    # We use 'through' attribute to customize our pivot table
    is_valid = models.BooleanField(default=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def get_description(self):
        # creating a function in order to lower the description while returning it
        return self.description.lower()  # TODO ask

    def __str__(self):
        return self.title
    # show the object by its title

    # def clean(self):
    #     raise ValidationError('Not good')


class MovieCrew(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('movie', 'crew', 'role')
        # used to make two or more model fields to be true and unique
        # Meta classes are used to add or change a behavior in a class
