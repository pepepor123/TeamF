# Generated by Django 3.1.1 on 2020-09-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ahare',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wokashi',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]