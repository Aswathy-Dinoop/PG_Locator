# Generated by Django 5.0.2 on 2024-02-15 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0002_ownerregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADD_PG_INFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appartment_name', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('facilities', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(max_length=50, null=True, upload_to='')),
                ('transport', models.CharField(max_length=50, null=True)),
                ('food', models.CharField(max_length=50, null=True)),
                ('pgowner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgapp.ownerregistration')),
            ],
        ),
    ]
