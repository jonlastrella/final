# Generated by Django 2.2 on 2021-06-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0008_auto_20210531_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='meet',
            field=models.CharField(default='', max_length=255),
        ),
    ]
