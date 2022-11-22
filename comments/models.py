from django.db import models
from django.conf import settings
from movies.models import Movie, Crew


# comment models will be abstracted from model below
class AbstractComment(models.Model):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40

    COMMENT_STATUS_CHOICES = (
        (CREATED, 'Created'), (APPROVED, 'Approved'), (REJECTED, 'Rejected'), (DELETED, 'Deleted')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s')
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    validated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='validated_%(class)s')
    # 'validated_by' shows who accepted the comment to be published
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=COMMENT_STATUS_CHOICES, default=CREATED)

    class Meta:
        abstract = True


# the below class is used for commenting on movies
class MovieComment(AbstractComment):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


# the below class is used for commenting on crew members
class CrewComment(AbstractComment):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
