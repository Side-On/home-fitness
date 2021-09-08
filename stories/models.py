from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Story(models.Model):

    class Meta:
        verbose_name_plural = 'Stories'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story_title = models.CharField(max_length=254, null=False, blank=False)
    story_content = models.TextField(max_length=1200, null=False, blank=False)

    def __str__(self):
        return f'Story written by {self.user}'
