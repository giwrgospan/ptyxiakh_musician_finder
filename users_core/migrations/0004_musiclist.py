# Generated by Django 2.1.4 on 2019-04-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0003_remove_profile_f_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_category', models.CharField(choices=[('Rock', 'Rock'), ('Punk', 'Punk'), ('Pop', 'Pop'), ('Hip-Hop', 'Hip-Hop')], max_length=100)),
            ],
        ),
    ]
