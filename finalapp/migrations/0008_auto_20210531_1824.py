# Generated by Django 2.2 on 2021-06-01 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0007_about_meet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='meet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='motto',
            field=models.CharField(max_length=55),
        ),
    ]
