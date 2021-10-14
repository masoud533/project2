# Generated by Django 3.2.6 on 2021-10-09 10:53

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('slide_image', models.ImageField(upload_to='panel/images/backgrounds/')),
                ('slider_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='OurSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('counter', models.CharField(max_length=32)),
                ('feature', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='panel/images/backgrounds/')),
                ('position', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('header_image', models.ImageField(upload_to='panel/images/backgrounds/')),
                ('thumbnail', models.ImageField(upload_to='panel/images/backgrounds/')),
                ('header_text', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('text', models.TextField()),
                ('Strategy', models.TextField()),
                ('Development', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]