from django.db import models
import datetime
# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, max_length=100, unique=True)
    description = models.TextField()
    posted_date = models.DateTimeField(
        auto_now_add=True)
    salary = models.IntegerField()

    def __str__(self):
        return self.title
