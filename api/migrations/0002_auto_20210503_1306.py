# Generated by Django 3.2 on 2021-05-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='artist',
            field=models.CharField(default='artist', max_length=1000),
        ),
        migrations.AddField(
            model_name='video',
            name='song',
            field=models.CharField(default='song', max_length=1000),
        ),
    ]
