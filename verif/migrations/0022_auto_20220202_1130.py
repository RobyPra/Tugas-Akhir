# Generated by Django 3.2.6 on 2022-02-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0021_auto_20220202_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastface',
            name='img',
        ),
        migrations.AddField(
            model_name='log',
            name='cosine',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='euclidean',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
