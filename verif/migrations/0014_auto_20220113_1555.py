# Generated by Django 3.2.6 on 2022-01-13 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0013_auto_20220113_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='recorded_by',
        ),
        migrations.AddField(
            model_name='face',
            name='recorded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='verif.ipcam'),
        ),
        migrations.AlterField(
            model_name='ipcam',
            name='rtsp',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
    ]
