# Generated by Django 2.2 on 2022-01-30 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_items_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='prod',
            new_name='prodt',
        ),
    ]
