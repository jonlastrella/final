# Generated by Django 2.2 on 2021-05-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0004_about_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='motto',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]
