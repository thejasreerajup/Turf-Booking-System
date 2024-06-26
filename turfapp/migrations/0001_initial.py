# Generated by Django 5.0.4 on 2024-05-05 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=500)),
                ('password', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='turf_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(default='', max_length=500)),
                ('category', models.CharField(default='', max_length=500)),
                ('description', models.CharField(default='', max_length=500)),
                ('location', models.CharField(default='', max_length=500)),
                ('mobile', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=500)),
                ('price', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(upload_to='files')),
                ('facility', models.CharField(default='', max_length=500)),
                ('specification', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='user_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('address', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=500)),
                ('contact', models.CharField(default='', max_length=500)),
                ('password', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='booking_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeto', models.CharField(default='', max_length=30)),
                ('timefrom', models.CharField(default='', max_length=30)),
                ('date', models.CharField(default='', max_length=30)),
                ('status', models.CharField(default='', max_length=30)),
                ('turfid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfapp.turf_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turfapp.user_tb')),
            ],
        ),
    ]
