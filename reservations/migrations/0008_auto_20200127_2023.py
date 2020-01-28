# Generated by Django 2.2.9 on 2020-01-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20200120_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('confirmed', 'Comfirmed')], default='pending', max_length=12),
        ),
    ]
