# Generated by Django 3.2.6 on 2021-10-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20211010_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSwiper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]