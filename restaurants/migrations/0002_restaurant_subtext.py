# Generated by Django 3.2.13 on 2022-11-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='subtext',
            field=models.CharField(default=0, max_length=140),
            preserve_default=False,
        ),
    ]