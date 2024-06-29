from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="articles/",default='')
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")


    def __str__(self):
        return self.title
    