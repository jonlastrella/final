# Generated by Django 2.2 on 2021-06-01 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0005_about_motto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='motto',
            field=models.CharField(default='Hi!', max_length=55),
        ),
    ]