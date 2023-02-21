from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    def __str__(self):
        return self.city


class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, max_length=100, unique=True)
    description = RichTextUploadingField()
    posted_date = models.DateTimeField(
        auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    location = models.OneToOneField(
        Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)
    type = models.CharField(max_length=10, null=False,
                            choices=JOB_TYPE_CHOICES, default='Full Time')

    def __str__(self):
        return self.title
