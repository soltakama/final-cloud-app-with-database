# Generated by Django 3.1.3 on 2021-10-22 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_choice_is_correct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
    ]
