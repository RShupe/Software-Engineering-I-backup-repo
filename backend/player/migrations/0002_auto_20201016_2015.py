# Generated by Django 3.1.2 on 2020-10-17 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='completed',
        ),
    ]