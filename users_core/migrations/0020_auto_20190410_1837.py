# Generated by Django 2.1.4 on 2019-04-10 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0019_auto_20190410_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users_core.Profile'),
        ),
    ]