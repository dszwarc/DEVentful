# Generated by Django 4.1.7 on 2023-04-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_merge_20230419_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='phone',
            field=models.IntegerField(default=1234567890),
        ),
    ]
