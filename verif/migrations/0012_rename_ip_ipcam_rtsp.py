# Generated by Django 3.2.6 on 2022-01-13 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0011_ipcam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipcam',
            old_name='ip',
            new_name='rtsp',
        ),
    ]
