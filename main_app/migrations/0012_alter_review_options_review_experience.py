# Generated by Django 4.2 on 2023-04-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='review',
            name='experience',
            field=models.CharField(choices=[('E', 'Excellent'), ('A', 'Average'), ('T', 'Terrible')], default='A', max_length=1),
        ),
    ]
