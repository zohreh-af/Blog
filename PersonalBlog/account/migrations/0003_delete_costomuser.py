# Generated by Django 5.0.3 on 2024-10-01 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_user_costomuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CostomUser',
        ),
    ]
