from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, default='')
    content = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    category = models.CharField(max_length=255, default='')

class Comment(models.Model):
    post = models.ForeingKey(Post)
    author = models.CharField(max_length=100, default='')
    content = models.TextField()
    date = models.DateTimeField()