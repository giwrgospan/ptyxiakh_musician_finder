# Generated by Django 2.1.4 on 2019-04-10 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0016_auto_20190410_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_core.Profile'),
        ),
    ]
