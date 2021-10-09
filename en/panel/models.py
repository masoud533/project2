from django.db import models
from datetime import datetime
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


TYPE_CHOICES = (
    ('M', 'Month'),
    ('Y', 'Years'),
)


class Plans(models.Model):
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    feature = models.TextField(blank=True)
    count = models.CharField(max_length=32)
    count_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    full_name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='panel/images/backgrounds/')
    position = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class WhoWeAre(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField(blank=False)
    Strategy = models.TextField(blank=False)
    Development = models.TextField(blank=False)

    def __str__(self):
        return self.title


class WhatWeDo(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class WorkProcess(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class OurSkills(models.Model):
    title = models.CharField(max_length=32)
    counter = models.CharField(max_length=32)
    feature = models.TextField(blank=True)

    def __str__(self):
        return self.title
