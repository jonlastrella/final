# Generated by Django 2.2 on 2021-06-12 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0025_auto_20210612_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='file',
            field=models.FileField(default='media/static/img/default.png', upload_to='user_images'),
        ),
    ]