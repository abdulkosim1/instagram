# Generated by Django 4.1.7 on 2023-03-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_buyer',
            field=models.BooleanField(default=False),
        ),
    ]
