# Generated by Django 3.2.6 on 2021-10-10 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_rename_feesback_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.ImageField(upload_to='panel/images/avatars/'),
        ),
    ]
