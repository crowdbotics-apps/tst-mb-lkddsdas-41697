# Generated by Django 2.2.28 on 2023-06-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20230629_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hello',
            name='ksdjjd',
        ),
        migrations.AddField(
            model_name='hello',
            name='ksdjjdkhj',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
