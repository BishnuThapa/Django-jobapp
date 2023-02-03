from django.db import models

# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
