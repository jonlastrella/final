# Generated by Django 2.2 on 2021-06-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0012_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='file',
            field=models.FileField(default=None, upload_to='user_images'),
        ),
    ]
