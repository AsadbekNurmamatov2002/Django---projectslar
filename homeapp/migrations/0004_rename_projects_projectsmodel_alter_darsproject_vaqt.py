# Generated by Django 4.2.3 on 2023-11-28 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_alter_darsproject_vaqt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='ProjectsModel',
        ),
        migrations.AlterField(
            model_name='darsproject',
            name='vaqt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 28, 21, 51, 38, 472420)),
        ),
    ]
