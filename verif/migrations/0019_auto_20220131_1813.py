# Generated by Django 3.2.6 on 2022-01-31 11:13

from django.db import migrations, models
import verif.models


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0018_alter_lastface_last_face'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='log',
        ),
        migrations.RemoveField(
            model_name='log',
            name='visitor',
        ),
        migrations.AddField(
            model_name='log',
            name='face_log',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='log',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=verif.models.face_directory_path),
        ),
        migrations.DeleteModel(
            name='Face',
        ),
    ]
