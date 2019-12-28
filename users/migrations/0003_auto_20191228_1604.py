# Generated by Django 2.2.8 on 2019-12-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191227_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'female'), ('male', 'male'), ('other', 'other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('kr', 'Korean'), ('en', 'English')], max_length=2),
        ),
    ]
