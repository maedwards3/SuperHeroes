# Generated by Django 3.1.8 on 2021-06-03 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0002_superheroes_catch_phrase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='superheroes',
            old_name='catch_phrase',
            new_name='catchphrase',
        ),
    ]
