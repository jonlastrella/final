# Generated by Django 2.2 on 2021-06-12 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0019_auto_20210611_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profilepicture', serialize=False, to='finalapp.User'),
        ),
    ]
