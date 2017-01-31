from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """docstring for post"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    # def __init__(self, arg=None):
    #     super(Post, self).__init__()
    #     self.arg = arg

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
