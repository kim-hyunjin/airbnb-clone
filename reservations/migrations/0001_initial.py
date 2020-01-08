# Generated by Django 2.2.8 on 2020-01-04 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('status', models.CharField(choices=[('confirmed', 'Comfirmed'), ('canceled', 'Canceled'), ('pending', 'Pending')], default='pending', max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]