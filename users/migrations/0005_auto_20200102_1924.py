# Generated by Django 2.2.8 on 2020-01-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200102_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('other', 'other'), ('male', 'male'), ('female', 'female')], max_length=10),
        ),
    ]
