# Generated by Django 2.2 on 2021-05-31 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='mood',
            field=models.CharField(default='No Mood', max_length=7),
        ),
    ]
