# Generated by Django 4.0.2 on 2022-02-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=200)),
                ('esal', models.FloatField()),
                ('eaddress', models.CharField(max_length=200)),
            ],
        ),
    ]
