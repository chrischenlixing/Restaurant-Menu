# Generated by Django 4.2 on 2023-05-06 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_calories_item_carbs_item_fats_item_protein'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='item',
            name='carbs',
        ),
        migrations.RemoveField(
            model_name='item',
            name='fats',
        ),
        migrations.RemoveField(
            model_name='item',
            name='protein',
        ),
    ]
