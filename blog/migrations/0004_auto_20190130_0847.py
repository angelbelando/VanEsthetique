# Generated by Django 2.1.5 on 2019-01-30 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_title_it'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='title_fr',
            new_name='intro_fr',
        ),
        migrations.RenameField(
            model_name='blogpage',
            old_name='title_it',
            new_name='intro_it',
        ),
    ]
