import json

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class HomeSlider(models.Model):
    title = models.CharField(max_length=32)
    slide_image = models.ImageField(upload_to='panel/images/backgrounds/')
    slider_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=32)
    header_image = models.ImageField(upload_to='panel/images/backgrounds/')
    thumbnail = models.ImageField(upload_to='panel/images/backgrounds/')
    header_text = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Plans(models.Model):
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    feature = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
