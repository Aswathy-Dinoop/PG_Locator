# Generated by Django 4.2.4 on 2024-02-26 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0006_addtocart_pg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtocart',
            old_name='pg',
            new_name='pg_info',
        ),
    ]
