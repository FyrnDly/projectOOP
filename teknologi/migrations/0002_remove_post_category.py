# Generated by Django 4.1.2 on 2022-11-11 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teknologi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]