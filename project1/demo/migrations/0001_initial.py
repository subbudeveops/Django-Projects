# Generated by Django 4.0 on 2021-12-31 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='images/')),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
