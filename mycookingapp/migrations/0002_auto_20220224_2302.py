# Generated by Django 2.2.4 on 2022-02-24 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycookingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SavedRecipes',
            new_name='Recipe',
        ),
    ]
