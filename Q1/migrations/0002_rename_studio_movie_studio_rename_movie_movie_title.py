# Generated by Django 5.1.4 on 2025-01-03 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Q1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Studio',
            new_name='studio',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie',
            new_name='title',
        ),
    ]
