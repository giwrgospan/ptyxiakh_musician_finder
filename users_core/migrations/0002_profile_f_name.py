# Generated by Django 2.1.4 on 2019-03-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='f_name',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
