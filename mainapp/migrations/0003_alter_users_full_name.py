# Generated by Django 5.1.4 on 2025-02-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_users_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='full_name',
            field=models.CharField(max_length=150),
        ),
    ]
