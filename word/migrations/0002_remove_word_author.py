# Generated by Django 5.0.1 on 2024-01-13 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='author',
        ),
    ]
