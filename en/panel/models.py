from django.db import models
from datetime import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class HomeSlider(models.Model):
    title = models.CharField(max_length=32)
    slide_image = models.ImageField(upload_to='panel/images/backgrounds/')
    slider_text = models.CharField(max_length=200)
    button_text = models.CharField(max_length=32)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
