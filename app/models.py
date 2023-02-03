from django.db import models
import datetime
# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    posted_date = models.DateTimeField(
        auto_now_add=True)
    salary = models.IntegerField()

    def __str__(self):
        return self.title
