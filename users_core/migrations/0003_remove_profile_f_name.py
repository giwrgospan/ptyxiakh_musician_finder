# Generated by Django 2.1.4 on 2019-03-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0002_profile_f_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='f_name',
        ),
    ]