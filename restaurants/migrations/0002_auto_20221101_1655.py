# Generated by Django 3.2.13 on 2022-11-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='tag1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='tag5',
            field=models.TextField(),
        ),
    ]