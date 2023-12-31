# Generated by Django 4.2.3 on 2023-11-29 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_rename_projects_projectsmodel_alter_darsproject_vaqt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUrta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=250)),
                ('title2', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('yunalish', models.CharField(max_length=25)),
                ('rasim', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='darsproject',
            name='vaqt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 29, 21, 10, 59, 519811)),
        ),
    ]
