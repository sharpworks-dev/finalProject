# Generated by Django 3.1.3 on 2020-12-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0006_auto_20201209_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]