from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

TYPE_CHOICES = (
    ('M', 'Month'),
    ('Y', 'Years'),
)


class HomeSlider(models.Model):
    title = models.CharField(max_length=32, verbose_name = 'عنوان')
    slide_image = models.ImageField(upload_to='panel/images/backgrounds/', verbose_name = 'ویدیو')
    slider_text = models.TextField(blank=True, verbose_name = 'متن اسلایدر')
    button_text = models.TextField(blank=True, verbose_name = 'متن دکمه')
    pub_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name = 'تاریخ انتشار')

    class Meta:
        verbose_name = "اسلایدر هدر صفحه اصلی"
        verbose_name_plural = "اسلایدر های هدر صفحه اصلی"

    def __str__(self):
        return self.title


class BodySlider(models.Model):
    title = models.CharField(max_length=32, verbose_name = 'عنوان')
    slide_image = models.ImageField(upload_to='panel/images/backgrounds/', verbose_name = 'تصویر')
    slider_text = models.TextField(blank=True, verbose_name = 'متن اسلایدر')
    pub_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name = 'تاریخ انتشار')

    class Meta:
        verbose_name = "اسلایدر بدنه صفحه اصلی"
        verbose_name_plural = "اسلایدر های بدنه صفحه اصلی"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    under_title = models.CharField(max_length=32, verbose_name='زیر متن')
    header_image = models.ImageField(upload_to='panel/images/backgrounds/', verbose_name='تصویر تیتر')
    thumbnail = models.ImageField(upload_to='panel/images/backgrounds/', verbose_name='تصویر بندانگشتی')
    header_text = models.CharField(max_length=200, verbose_name='متن تیتر')
    content = RichTextUploadingField(blank=True, null=True, verbose_name='محتوا')
    pub_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"

    def __str__(self):
        return self.title


class Plans(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    old_price = models.IntegerField(verbose_name='قیمت قدیمی')
    price = models.IntegerField(verbose_name='قیمت')
    feature = models.TextField(blank=True, verbose_name='ویژگی ها')
    count = models.CharField(max_length=32, verbose_name='دوره پرداخت')
    count_type = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name='نوع دوره پرداخت')
    pub_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = "پلن فروش"
        verbose_name_plural = "پلن های فروش"

    def __str__(self):
        return self.title


class OurTeam(models.Model):
    full_name = models.CharField(max_length=32, verbose_name='نام و نام خانوادگی')
    image = models.ImageField(upload_to='panel/images/backgrounds/', verbose_name='تصویر')
    position = models.CharField(max_length=32, verbose_name='مقعیت شقلی')
    description = models.TextField(blank=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = "اعضای تیم"
        verbose_name_plural = "اعضای تیم"

    def __str__(self):
        return self.full_name


class WhoWeAre(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    text = models.TextField(blank=False, verbose_name='متن')
    Strategy_title = models.TextField(blank=False, verbose_name='عنوان استراتژی')
    Strategy = models.TextField(blank=False, verbose_name='ویژگی های استراتژی')
    Development_title = models.TextField(blank=False, verbose_name='عنوان دولوپمنت')
    Development = models.TextField(blank=False, verbose_name='ویژگی های دولوپمنت')

    class Meta:
        verbose_name = "ما کی هستیم"
        verbose_name_plural = "ما کی هستیم"

    def __str__(self):
        return self.title


class WhatWeDo(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    text = models.TextField(blank=True, verbose_name='متن')

    class Meta:
        verbose_name = "آنچه ما انجام می دهیم"
        verbose_name_plural = "آنچه ما انجام می دهیم"

    def __str__(self):
        return self.title


class WorkProcess(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    text = models.TextField(blank=True, verbose_name='متن')

    class Meta:
        verbose_name = "طراحی حرفه ای"
        verbose_name_plural = "طراحی حرفه ای"

    def __str__(self):
        return self.title


class OurSkills(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    counter = models.CharField(max_length=32, verbose_name='شمارنده')
    feature = models.TextField(blank=True, verbose_name='ویژگی ها')

    class Meta:
        verbose_name = "آمار و ارقام"
        verbose_name_plural = "آمار و ارقام"

    def __str__(self):
        return self.title


class FooterSwiper(models.Model):
    text = models.TextField(blank=True, verbose_name='متن')

    class Meta:
        verbose_name = "سوایپر پاورقی"
        verbose_name_plural = "سوایپر پاورقی"

    def __str__(self):
        return self.text


class About(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    text = models.TextField(blank=True, verbose_name='متن')
    image = models.ImageField(upload_to='panel/images/backgrounds/', verbose_name='تصویر')

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.title


class FeedBack(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    text = models.TextField(blank=True, verbose_name='متن')
    full_name = models.CharField(max_length=32, verbose_name='نام و نام خانوادگی')
    image = models.ImageField(upload_to='panel/images/avatars/', verbose_name='آواتار')
    position = models.CharField(max_length=32, verbose_name='جایگاه شغلی')

    class Meta:
        verbose_name = "بازخورد"
        verbose_name_plural = "بازخورد ها"

    def __str__(self):
        return self.title


class OtherWorkProcess(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    text = models.TextField(blank=True, verbose_name='متن')

    class Meta:
        verbose_name = "دیگر طراحی حرفه ای"
        verbose_name_plural = "دیگر طراحی حرفه ای"

    def __str__(self):
        return self.title
